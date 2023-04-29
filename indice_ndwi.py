# -*- coding: utf-8 -*-
"""
/***************************************************************************
 IndiceNDWI
                                 A QGIS plugin
 Este complemento calcula el índice NDWI con las imágenes del Landsat 8.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2022-11-22
        git sha              : $Format:%H$
        copyright            : (C) 2022 by Francisca Ruiz-Tagle Santander y Keyla Alencar da Silva - UTEM/UNR
        email                : fa.ruiztaglest@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import os
import numpy as np
from math import *
from osgeo import gdal 
from shutil import rmtree
from qgis.PyQt.QtGui import QIcon
from PyQt5.QtMultimedia import QSound
from qgis.core import QgsRasterLayer, Qgis
from qgis.PyQt.QtWidgets import QAction, QLabel
from PyQt5.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
from PyQt5.QtWidgets import QAction,QFileDialog, QDialog, QLabel, QMessageBox, QMenu, QSizePolicy

# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .indice_ndwi_dialog import IndiceNDWIDialog
import os.path

class Instrucciones(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        
        self.setMaximumSize(QtCore.QSize(1250,400))
        self.setMinimumSize(QtCore.QSize(1250,400))
        self.setWindowTitle("Instrucciones")
        self.etiqueta = QLabel(self)
        self.etiqueta.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.etiqueta.move(50,20)
        self.etiqueta.setStyleSheet("border: 1px solid black; padding: 25px; font: 75 9pt 'Calibri';border-radius: 10px 10px 10px 10px;")

class IndiceNDWI:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        self.dialogo = Instrucciones()
        self.archivo_MTL = []
        self.rutas_bandas = []
        self.rutas_bandas_corr = []
        self.estado_corr = "inactivo"
        self.ruta_guardar = []
        self.sound = QSound(os.path.dirname(__file__)+"/exito.wav")

        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'IndiceNDWI_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Moisture and Water Index')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('IndiceNDWI', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """
        self.dlg = IndiceNDWIDialog
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/indice_ndwi/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Calculate Moisture and Water Index'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Moisture and Water Index'),
                action)
            self.iface.removeToolBarIcon(action)


    def inst(self):
        self.dialogo.etiqueta.setText("\tINSTRUCCIONES\n\n1. Asegurarse que las imágenes satelitales que usará sean exclusivamente de Landsat 8.\n2. Determinar si el proceso requiere corrección atmosférica:\n\nEn caso de requerir:\n\t- Dejar desmarcado la opción “Corrección realizada”.\n\t- Pulsar el icono de la opción “Seleccionar imágenes Landsat 8” y seleccionar todas las bandas satelitales de Landsat 8 (debe cerciorarse que estén las bandas 3, 5 y 6).\n\t- Pulsar el icono de la opción “Seleccionar archivo MTL” y escoger el archivo MTL (formato *.txt).\n\nEn caso de no requerir:\n\t- Marcar la opción “Corrección realizada”.\n\t- Pulsar el icono de la opción “Seleccionar imágenes corregidas Landsat 8” y seleccionar todas las bandas satelitales de Landsat 8 (debe cerciorarse que estén las bandas 3, 5 y 6).\n\n3. Pulsar el icono de la opción “Guardar NDWI”, escoger el directorio donde desea guardar y escribir el nombre de la carpeta que contendrá los resultados.\n4. Pulsar el botón “Ejecutar” (es normal que el proceso demore un par de segundos).")
        self.dialogo.exec_()


    def abrirTIF(self,rutas_bandas):
        archivo, _ = QFileDialog.getOpenFileNames(self.dlg, 'Abrir archivo', '', 'TIF file .TIF (*.TIF)')
        
        if archivo:
            mensaje = self.dlg.cuadroTIF.setText(archivo[0])
            self.dlg.btn_abrirTIF.setText(mensaje)
        for i in archivo:
            if i not in self.rutas_bandas:
                self.rutas_bandas.append(i)

        if len(self.rutas_bandas) > 0 and self.estado_corr == 'inactivo':

            #filtro de bandas para mostrar anuncio 
            bandas_necesarias = ["B3", "B5", "B6"]
            bandas_faltantes = []

            for banda in bandas_necesarias:
                if not any(banda in ruta for ruta in self.rutas_bandas):
                    bandas_faltantes.append(banda)

            if bandas_faltantes:
                mensaje = f"Las siguientes bandas no están presentes: {', '.join(bandas_faltantes)}"
                QMessageBox.warning(self.dlg, "Aviso", mensaje)
            
        return rutas_bandas
    
      
    def abrirMTL(self,archivo_MTL):
        archivo, _ = QFileDialog.getOpenFileNames(self.dlg, 'Abrir archivo','', 'MTL file .txt (*.txt)')

        if archivo:
            mensaje = self.dlg.cuadroMTL.setText(archivo[0])
            self.dlg.btn_abrirMTL.setText(mensaje)
            self.archivo_MTL.append(archivo[0])

            #Abrir el archivo en modo lectura
            with open(self.archivo_MTL[0], "r") as file:
            # Leer el contenido del archivo y almacenarlo en una variable
                content = file.read()

               # Verificar si la palabra "LC08" está presente en el contenido del archivo
                if "LC08" in content:

                    # Generar la función
                    pass
                else:
                    mensaje = "El MTL ingresado NO corresponde al satélite Landsat 8"
                    QMessageBox.warning(self.dlg, "Aviso", mensaje)
                    self.archivo_MTL.clear()

        return archivo_MTL
    

    def estado(self):
        if self.dlg.btn_correccion.isChecked()==False:

            self.estado_corr = "inactivo"
            self.dlg.cuadroTIF.setEnabled(True)
            self.dlg.btn_abrirTIF.setEnabled(True)
            self.dlg.cuadroMTL.setEnabled(True)
            self.dlg.btn_abrirMTL.setEnabled(True)
            self.dlg.cuadroBandasCorregidas.setEnabled(False)
            self.dlg.btn_abrirCORR.setEnabled(False)
            self.dlg.msj_TIF.setEnabled(True)
            self.dlg.msj_MTL.setEnabled(True)
            self.dlg.msj_CORR.setEnabled(False)
            
        else:
            self.estado_corr = "activo"
            self.dlg.cuadroTIF.setEnabled(False)
            self.dlg.btn_abrirTIF.setEnabled(False)
            self.dlg.cuadroMTL.setEnabled(False)
            self.dlg.btn_abrirMTL.setEnabled(False)
            self.dlg.cuadroBandasCorregidas.setEnabled(True)
            self.dlg.btn_abrirCORR.setEnabled(True)
            self.dlg.msj_TIF.setEnabled(False)
            self.dlg.msj_MTL.setEnabled(False)
            self.dlg.msj_CORR.setEnabled(True)


    def estado_ejecutar(self):
        if len(self.rutas_bandas) > 0 and self.estado_corr == 'inactivo':

            if len(self.archivo_MTL) > 0 and self.archivo_MTL[0]:
                #Abrir el archivo en modo lectura
                with open(self.archivo_MTL[0], "r") as file:
                # Leer el contenido del archivo y almacenarlo en una variable
                    content = file.read()
                    # Verificar si la palabra "LC08" está presente en el contenido del archivo
                    if "LC08" in content:
        
                        if len(self.ruta_guardar) > 0 and self.ruta_guardar[0]:
                            self.dlg.btn_ejecutar.setEnabled(True)
                            self.dlg.aviso_ejecutar.setVisible(False)
                            self.message_bar = self.iface.messageBar()
                            self.message_bar.pushMessage("ADVERTENCIA:", "El proceso de cálculo y generación de archivos puede demorar varios segundos, por favor esperar sonido y/o mensaje de éxito (IMPORTANTE: NO INTERRUMPA LA EJECUCIÓN)", level=Qgis.Warning, duration=-1)

            elif len(self.archivo_MTL) == 0:
                #filtro de bandas para mostrar anuncio 
                bandas_necesarias = ["B3", "B5", "B6"]
                bandas_faltantes = []

                for banda in bandas_necesarias:
                    if not any(banda in ruta for ruta in self.rutas_bandas):
                        bandas_faltantes.append(banda)

                if bandas_faltantes:
                    mensaje = f"Las siguientes bandas no están presentes: {', '.join(bandas_faltantes)}"
                    QMessageBox.warning(self.dlg, "Aviso", mensaje)

        if len(self.rutas_bandas_corr) > 0 and self.estado_corr == 'activo':
            
            if len(self.ruta_guardar) > 0 and self.ruta_guardar[0]:
                self.dlg.btn_ejecutar.setEnabled(True)
                self.dlg.aviso_ejecutar.setVisible(False)  
                self.message_bar = self.iface.messageBar()
                self.message_bar.pushMessage("ADVERTENCIA:", "El proceso de cálculo y generación de archivos puede demorar varios segundos, por favor esperar sonido y/o mensaje de éxito (IMPORTANTE: NO INTERRUMPA LA EJECUCIÓN)", level=Qgis.Warning, duration=-1)  


    def abrirCORR(self,rutas_bandas_corr): 
        archivo, _ = QFileDialog.getOpenFileNames(self.dlg, 'Abrir archivo', '', 'TIF file .TIF (*.TIF)')

        if archivo:
            mensaje = self.dlg.cuadroBandasCorregidas.setText(archivo[0])
            self.dlg.btn_abrirCORR.setText(mensaje)
        for i in archivo:
            if i not in self.rutas_bandas_corr:
                self.rutas_bandas_corr.append(i)

        if len(self.rutas_bandas_corr) > 0 and self.estado_corr == 'activo':

            #filtro de bandas para mostrar anuncio 
            bandas_necesarias = ["B3", "B5", "B6"]
            bandas_faltantes = []

            for banda in bandas_necesarias:
                if not any(banda in ruta for ruta in self.rutas_bandas_corr):
                    bandas_faltantes.append(banda)

            if bandas_faltantes:
                mensaje = f"Las siguientes bandas no están presentes: {', '.join(bandas_faltantes)}"
                QMessageBox.warning(self.dlg, "Aviso", mensaje)

        return rutas_bandas_corr
    
    
    def guardar(self, ruta_guardar):
        archivo = QFileDialog.getSaveFileName(self.dlg,'Guardar archivo')

        if archivo:
            mensaje = self.dlg.cuadroGuardar.setText(archivo[0])
            self.dlg.btn_guardar.setText(mensaje)
        self.ruta_guardar.append(archivo[0])
        
        return ruta_guardar


    def sonido_termino(self):
        self.sound.play()


    def ejecutar(self):
        #creacion de la carpeta general 
        os.mkdir(self.ruta_guardar[0])

        if self.estado_corr == "activo":

            for i in self.rutas_bandas_corr:
                if ("B3.TIF" in i):
                    banda_3 = i
                if ("B5.TIF" in i):
                    banda_5 = i
                if ("B6.TIF" in i):
                    banda_6 = i

            self.GUARDAR_NDWI(banda_3,banda_6,banda_5)
            self.message_bar.clearWidgets()
            self.message_bar = self.iface.messageBar()
            self.message_bar.pushMessage("ANUNCIO:", "Se generó exitosamente el cálculo del índice NDWI en formato .TIF a través de los métodos Xu, Gao y McFeeters.", level=Qgis.Success, duration=0)
            self.limpiar()

        if self.estado_corr == "inactivo":

            ruta_MTL = self.archivo_MTL[0]
            bandas = self.rutas_bandas

            self.filtro(ruta_MTL,bandas)
            self.GUARDAR_NDWI(self.ruta_guardar[0] + '/correcciones/correccion_atmosferica_B3.TIF', self.ruta_guardar[0] + '/correcciones/correccion_atmosferica_B6.TIF', self.ruta_guardar[0] + '/correcciones/correccion_atmosferica_B5.TIF')
            rmtree(self.ruta_guardar[0] + '/correcciones')
            self.message_bar.clearWidgets()
            self.message_bar = self.iface.messageBar()
            self.message_bar.pushMessage("ANUNCIO:", "Se generó exitosamente el cálculo del índice NDWI en formato .TIF a través de los métodos Xu, Gao y McFeeters.", level=Qgis.Success,duration=0)
            self.limpiar() 


    def cerrar(self): 
        self.limpiar()
        self.dlg.close()
        self.dlg.btn_ejecutar.setEnabled(False)
        

    def limpiar(self):
        self.dlg.cuadroTIF.clear()
        self.dlg.cuadroMTL.clear()
        self.dlg.cuadroBandasCorregidas.clear()
        self.dlg.cuadroGuardar.clear()
        self.archivo_MTL.clear()
        self.rutas_bandas.clear()
        self.rutas_bandas_corr.clear()
        self.ruta_guardar.clear()


    def guardar_raster(self,dataset,datasetPath,cols,rows,projection,geot):
        
        rasterSet = gdal.GetDriverByName('GTiff').Create(datasetPath, cols ,rows ,1,gdal.GDT_Float32)
        rasterSet.SetProjection(projection)
        rasterSet.SetGeoTransform(geot)
        rasterSet.GetRasterBand(1).WriteArray(dataset)
        rasterSet.GetRasterBand(1).SetNoDataValue(-999)
        rasterSet = None


    def correccion(self,n,banda,RADIANCE_MULT_BAND,RADIANCE_ADD_BAND,distancia_tierra_sol,cos_elevacion_solar,ESUN):

        B = gdal.Open(banda)
        dn = B.GetRasterBand(1).ReadAsArray().astype(np.float32) 
        RAD = RADIANCE_MULT_BAND * dn + RADIANCE_ADD_BAND
        REFLECTANCIA = (pi*RAD*distancia_tierra_sol**2)/(ESUN * cos_elevacion_solar)
        factor_escala =  55000  # 16000, 100000, ...
        REFLECTANCIA = REFLECTANCIA * factor_escala
        REFLECTANCIA= np.clip(REFLECTANCIA, 1, np.iinfo(np.uint16).max).astype(np.uint16)
        REFLECTANCIA[np.where(dn == 0)] = 0

        cols = B.RasterXSize
        rows = B.RasterYSize
        projection = B.GetProjection()
        geot = B.GetGeoTransform()

        self.guardar_raster(REFLECTANCIA, self.ruta_guardar[0] + f"/correcciones/correccion_atmosferica_B{n}.TIF",cols,rows,projection,geot)

          
    def filtro(self,path,archivo):
        #BANDAS
        for i in archivo:
            if ("B3.TIF" in i):
                banda_3 = i
            if ("B5.TIF" in i):
                banda_5 = i
            if ("B6.TIF" in i):
                banda_6 = i

        #FILTRO DEL MTL 
        with open (path, 'r') as file:
            archivo = file.read()

        array = []
        array = archivo.split()

        cont = 3
        pos = array.index('RADIANCE_MULT_BAND_3')
        RADIANCE_MULT_BAND = []
        i = 2
        while(cont < 7):
            RADIANCE_MULT_BAND.append(float(array[pos+ i]))
            i = i + 3
            cont = cont + 1

        cont = 3
        pos = array.index('RADIANCE_ADD_BAND_3')
        RADIANCE_ADD_BAND = []
        i = 2
        while(cont < 7):
            RADIANCE_ADD_BAND.append(float(array[pos+ i]))
            i = i + 3
            cont = cont + 1
        
        cont = 3
        pos = array.index('RADIANCE_MAXIMUM_BAND_3')
        RADIANCE_MAXIMUM_BAND = []
        i = 2
        while(cont < 7):
            RADIANCE_MAXIMUM_BAND.append(float(array[pos+ i]))
            i = i + 6
            cont = cont + 1
       
        cont = 3
        pos = array.index('REFLECTANCE_MAXIMUM_BAND_3')
        REFLECTANCE_MAXIMUM_BAND = []
        i = 2
        while(cont < 7):
            REFLECTANCE_MAXIMUM_BAND.append(float(array[pos+ i]))
            i = i + 6
            cont = cont + 1

        pos = array.index('SUN_ELEVATION')
        elevacion_solar = float(array[pos+2])

        pos = array.index('EARTH_SUN_DISTANCE')
        distancia_tierra_sol = float(array[pos+2])

        cos_elevacion_solar=cos((90-(elevacion_solar))*pi/180)

        cont = 3
        i = 0
        ESUN = []
        while(cont < 7):
            ESUN.append((pi*(distancia_tierra_sol)**2) * RADIANCE_MAXIMUM_BAND[i] / REFLECTANCE_MAXIMUM_BAND[i])
            cont = cont + 1
            i = i + 1

        os.mkdir(self.ruta_guardar[0] + '/correcciones')

        self.correccion(3,banda_3,RADIANCE_MULT_BAND[0],RADIANCE_ADD_BAND[0],distancia_tierra_sol,cos_elevacion_solar,ESUN[0])
        self.correccion(5,banda_5,RADIANCE_MULT_BAND[2],RADIANCE_ADD_BAND[2],distancia_tierra_sol,cos_elevacion_solar,ESUN[2])
        self.correccion(6,banda_6,RADIANCE_MULT_BAND[3],RADIANCE_ADD_BAND[3],distancia_tierra_sol,cos_elevacion_solar,ESUN[3])


    def NDWI (self, path_1, path_2, nombre_salida,banda_corr_1,banda_corr_2):

        dirB1 = path_1 
        dirB2 = path_2
        banda_1 = QgsRasterLayer(dirB1)
        banda_2 = QgsRasterLayer(dirB2)
        salida = self.ruta_guardar[0] + nombre_salida
        entradas = []
        banda_11 = QgsRasterCalculatorEntry()
        banda_11.ref = banda_corr_1
        banda_11.raster = banda_1
        banda_11.bandNumber = 1
        entradas.append(banda_11)
        banda_22 = QgsRasterCalculatorEntry()
        banda_22.ref = banda_corr_2
        banda_22.raster = banda_2
        banda_22.bandNumber = 1
        entradas.append(banda_22)

        calc = QgsRasterCalculator(f"('{banda_corr_1}'-'{banda_corr_2}')/('{banda_corr_1}'+'{banda_corr_2}')", salida, 'GTiff', banda_1.extent(), banda_1.width(), banda_1.height(), entradas)
        calc.processCalculation()
        
        
    def GUARDAR_NDWI(self,directorio, directorio1, directorio2):

        self.NDWI(directorio, directorio1, "/NDWI_XU.TIF", 'green@1','swir@1')
        self.NDWI(directorio2, directorio1, "/NDWI_GAO.TIF", 'nir@1','swir@1')
        self.NDWI(directorio, directorio2, "/NDWI_MCFEETERS.TIF", 'green@1','nir@1')

        self.iface.addRasterLayer(self.ruta_guardar[0] + '/NDWI_XU.TIF', "NDWI_XU")
        self.iface.addRasterLayer(self.ruta_guardar[0] + '/NDWI_GAO.TIF', "NDWI_GAO")
        self.iface.addRasterLayer(self.ruta_guardar[0] + '/NDWI_MCFEETERS.TIF', "NDWI_MCFEETERS")

  
    def run(self):
        """Run method that performs all the real work"""

        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        if self.first_start == True:
            self.first_start = False
            self.dlg = IndiceNDWIDialog()

            self.dlg.btn_abrirTIF.clicked.connect(self.abrirTIF)
            self.dlg.btn_abrirMTL.clicked.connect(self.abrirMTL)
            self.dlg.btn_guardar.clicked.connect(self.guardar)
            self.dlg.btn_ejecutar.clicked.connect(self.ejecutar)
            self.dlg.btn_cerrar.clicked.connect(self.cerrar)
            self.dlg.btn_abrirCORR.clicked.connect(self.abrirCORR)
            self.dlg.btn_correccion.clicked.connect(self.estado)
            self.dlg.cuadroBandasCorregidas.setEnabled(False)
            self.dlg.btn_abrirCORR.setEnabled(False)
            self.dlg.msj_CORR.setEnabled(False)
            self.dlg.btn_ejecutar.setEnabled(False)
            self.dlg.btn_inst.clicked.connect(self.inst)
            self.dlg.btn_ejecutar.clicked.connect(self.sonido_termino)
            self.dlg.btn_guardar.clicked.connect(self.estado_ejecutar)
            self.dlg.btn_abrirTIF.clicked.connect(self.estado_ejecutar)
            self.dlg.btn_abrirMTL.clicked.connect(self.estado_ejecutar)
            self.dlg.btn_abrirCORR.clicked.connect(self.estado_ejecutar)

            self.dlg.btn_abrirTIF.setToolTip("Selecciona las bandas")
            self.dlg.btn_abrirTIF.setToolTipDuration(3000)
            self.dlg.btn_abrirMTL.setToolTip("Abrir archivo")
            self.dlg.btn_abrirMTL.setToolTipDuration(3000)
            self.dlg.btn_correccion.setToolTip("Corrección atmosférica realizada")
            self.dlg.btn_correccion.setToolTipDuration(3000)
            self.dlg.btn_abrirCORR.setToolTip("Selecciona las bandas corregidas")
            self.dlg.btn_abrirCORR.setToolTipDuration(3000)
            self.dlg.btn_ejecutar.setToolTip("Ejecutar")
            self.dlg.btn_ejecutar.setToolTipDuration(3000)
            self.dlg.btn_guardar.setToolTip("Guardar resultados")
            self.dlg.btn_guardar.setToolTipDuration(3000)
            self.dlg.btn_cerrar.setToolTip("Cerrar")
            self.dlg.btn_cerrar.setToolTipDuration(3000)
            self.dlg.btn_inst.setToolTip("Leer instrucciones")
            self.dlg.btn_inst.setToolTipDuration(3000)

        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            pass
