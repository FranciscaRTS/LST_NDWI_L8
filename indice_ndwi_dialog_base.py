# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\indice_ndwi_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IndiceNDWIDialogBase(object):
    def setupUi(self, IndiceNDWIDialogBase):
        IndiceNDWIDialogBase.setObjectName("IndiceNDWIDialogBase")
        IndiceNDWIDialogBase.resize(771, 350)
        IndiceNDWIDialogBase.setMinimumSize(QtCore.QSize(771, 350))
        IndiceNDWIDialogBase.setMaximumSize(QtCore.QSize(771, 350))
        self.layoutWidget = QtWidgets.QWidget(IndiceNDWIDialogBase)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 751, 315))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.btn_inst = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_inst.setObjectName("btn_inst")
        self.horizontalLayout_7.addWidget(self.btn_inst)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_37 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        self.label_37.setMouseTracking(False)
        self.label_37.setStyleSheet("background-color : #919191; color : white")
        self.label_37.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_37.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_37.setObjectName("label_37")
        self.verticalLayout.addWidget(self.label_37)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.msj_TIF = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msj_TIF.sizePolicy().hasHeightForWidth())
        self.msj_TIF.setSizePolicy(sizePolicy)
        self.msj_TIF.setMinimumSize(QtCore.QSize(229, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.msj_TIF.setFont(font)
        self.msj_TIF.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.msj_TIF.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.msj_TIF.setObjectName("msj_TIF")
        self.horizontalLayout.addWidget(self.msj_TIF)
        self.cuadroTIF = QtWidgets.QLabel(self.layoutWidget)
        self.cuadroTIF.setEnabled(True)
        self.cuadroTIF.setFrameShape(QtWidgets.QFrame.Panel)
        self.cuadroTIF.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cuadroTIF.setText("")
        self.cuadroTIF.setObjectName("cuadroTIF")
        self.horizontalLayout.addWidget(self.cuadroTIF)
        self.btn_abrirTIF = QtWidgets.QToolButton(self.layoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/icons/imag_bruto.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_abrirTIF.setIcon(icon)
        self.btn_abrirTIF.setObjectName("btn_abrirTIF")
        self.horizontalLayout.addWidget(self.btn_abrirTIF)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.msj_MTL = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msj_MTL.sizePolicy().hasHeightForWidth())
        self.msj_MTL.setSizePolicy(sizePolicy)
        self.msj_MTL.setMinimumSize(QtCore.QSize(229, 0))
        self.msj_MTL.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.msj_MTL.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.msj_MTL.setObjectName("msj_MTL")
        self.horizontalLayout_2.addWidget(self.msj_MTL)
        self.cuadroMTL = QtWidgets.QLabel(self.layoutWidget)
        self.cuadroMTL.setFrameShape(QtWidgets.QFrame.Panel)
        self.cuadroMTL.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cuadroMTL.setText("")
        self.cuadroMTL.setObjectName("cuadroMTL")
        self.horizontalLayout_2.addWidget(self.cuadroMTL)
        self.btn_abrirMTL = QtWidgets.QToolButton(self.layoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/icons/MTL.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_abrirMTL.setIcon(icon1)
        self.btn_abrirMTL.setObjectName("btn_abrirMTL")
        self.horizontalLayout_2.addWidget(self.btn_abrirMTL)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_74 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy)
        self.label_74.setStyleSheet("background-color :#919191; color : white")
        self.label_74.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_74.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_74.setObjectName("label_74")
        self.verticalLayout.addWidget(self.label_74)
        self.btn_correccion = QtWidgets.QCheckBox(self.layoutWidget)
        self.btn_correccion.setChecked(False)
        self.btn_correccion.setTristate(False)
        self.btn_correccion.setObjectName("btn_correccion")
        self.verticalLayout.addWidget(self.btn_correccion)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.msj_CORR = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msj_CORR.sizePolicy().hasHeightForWidth())
        self.msj_CORR.setSizePolicy(sizePolicy)
        self.msj_CORR.setMinimumSize(QtCore.QSize(229, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.msj_CORR.setFont(font)
        self.msj_CORR.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.msj_CORR.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.msj_CORR.setObjectName("msj_CORR")
        self.horizontalLayout_3.addWidget(self.msj_CORR)
        self.cuadroBandasCorregidas = QtWidgets.QLabel(self.layoutWidget)
        self.cuadroBandasCorregidas.setEnabled(True)
        self.cuadroBandasCorregidas.setFrameShape(QtWidgets.QFrame.Panel)
        self.cuadroBandasCorregidas.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cuadroBandasCorregidas.setText("")
        self.cuadroBandasCorregidas.setObjectName("cuadroBandasCorregidas")
        self.horizontalLayout_3.addWidget(self.cuadroBandasCorregidas)
        self.btn_abrirCORR = QtWidgets.QToolButton(self.layoutWidget)
        self.btn_abrirCORR.setIcon(icon)
        self.btn_abrirCORR.setObjectName("btn_abrirCORR")
        self.horizontalLayout_3.addWidget(self.btn_abrirCORR)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_75 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy)
        self.label_75.setStyleSheet("background-color : #919191; color : white")
        self.label_75.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_75.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_75.setObjectName("label_75")
        self.verticalLayout.addWidget(self.label_75)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.msj_guardar = QtWidgets.QLabel(self.layoutWidget)
        self.msj_guardar.setObjectName("msj_guardar")
        self.horizontalLayout_4.addWidget(self.msj_guardar)
        self.cuadroGuardar = QtWidgets.QLabel(self.layoutWidget)
        self.cuadroGuardar.setFrameShape(QtWidgets.QFrame.Panel)
        self.cuadroGuardar.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cuadroGuardar.setText("")
        self.cuadroGuardar.setObjectName("cuadroGuardar")
        self.horizontalLayout_4.addWidget(self.cuadroGuardar)
        self.btn_guardar = QtWidgets.QToolButton(self.layoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/icons/guardar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_guardar.setIcon(icon2)
        self.btn_guardar.setObjectName("btn_guardar")
        self.horizontalLayout_4.addWidget(self.btn_guardar)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_ejecutar = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_ejecutar.setObjectName("btn_ejecutar")
        self.horizontalLayout_5.addWidget(self.btn_ejecutar)
        self.btn_cerrar = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.horizontalLayout_5.addWidget(self.btn_cerrar)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.retranslateUi(IndiceNDWIDialogBase)
        QtCore.QMetaObject.connectSlotsByName(IndiceNDWIDialogBase)

    def retranslateUi(self, IndiceNDWIDialogBase):
        _translate = QtCore.QCoreApplication.translate
        IndiceNDWIDialogBase.setWindowTitle(_translate("IndiceNDWIDialogBase", "Moisture and Water Index"))
        self.btn_inst.setText(_translate("IndiceNDWIDialogBase", "¿Cómo usar el complemento?"))
        self.label_37.setText(_translate("IndiceNDWIDialogBase", "Entrada de datos sin procesar "))
        self.msj_TIF.setText(_translate("IndiceNDWIDialogBase", "Seleccionar imágenes Landsat 8 "))
        self.btn_abrirTIF.setText(_translate("IndiceNDWIDialogBase", "..."))
        self.msj_MTL.setToolTip(_translate("IndiceNDWIDialogBase", "<html><head/><body><p>Select MTL file (if not in Landsat directory)</p></body></html>"))
        self.msj_MTL.setText(_translate("IndiceNDWIDialogBase", "Seleccionar archivo MTL"))
        self.btn_abrirMTL.setText(_translate("IndiceNDWIDialogBase", "..."))
        self.label_74.setText(_translate("IndiceNDWIDialogBase", "Corrección atmosférica (Radiancia y reflectancia TOA)"))
        self.btn_correccion.setToolTip(_translate("IndiceNDWIDialogBase", "<html><head/><body><p>Enable/Disable calculation of temperature in Celsius from thermal band</p></body></html>"))
        self.btn_correccion.setText(_translate("IndiceNDWIDialogBase", "Corrección realizada "))
        self.msj_CORR.setText(_translate("IndiceNDWIDialogBase", "Seleccionar imágenes corregidas Landsat 8 "))
        self.btn_abrirCORR.setText(_translate("IndiceNDWIDialogBase", "..."))
        self.label_75.setText(_translate("IndiceNDWIDialogBase", "Cálculo NDWI (Xu, Gao y McFeeters)"))
        self.msj_guardar.setText(_translate("IndiceNDWIDialogBase", "Guardar NDWI"))
        self.btn_guardar.setText(_translate("IndiceNDWIDialogBase", "..."))
        self.btn_ejecutar.setText(_translate("IndiceNDWIDialogBase", "Ejecutar"))
        self.btn_cerrar.setText(_translate("IndiceNDWIDialogBase", "Cerrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IndiceNDWIDialogBase = QtWidgets.QDialog()
    ui = Ui_IndiceNDWIDialogBase()
    ui.setupUi(IndiceNDWIDialogBase)
    IndiceNDWIDialogBase.show()
    sys.exit(app.exec_())
