# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt\configuredialog.ui'
#
# Created: Thu Dec 13 13:25:16 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        ConfigureDialog.setObjectName("ConfigureDialog")
        ConfigureDialog.resize(418, 303)
        self.gridLayout = QtGui.QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.configGroupBox = QtGui.QGroupBox(ConfigureDialog)
        self.configGroupBox.setTitle("")
        self.configGroupBox.setObjectName("configGroupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.configGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.preparedData_label = QtGui.QLabel(self.configGroupBox)
        self.preparedData_label.setObjectName("preparedData_label")
        self.gridLayout_2.addWidget(self.preparedData_label, 1, 1, 1, 1)
        self.preparedData_lineEdit = QtGui.QLineEdit(self.configGroupBox)
        self.preparedData_lineEdit.setObjectName("preparedData_lineEdit")
        self.gridLayout_2.addWidget(self.preparedData_lineEdit, 1, 2, 1, 1)
        self.preparedData_pushButton = QtGui.QPushButton(self.configGroupBox)
        self.preparedData_pushButton.setObjectName("preparedData_pushButton")
        self.gridLayout_2.addWidget(self.preparedData_pushButton, 1, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 178, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 2, 1, 1)
        self.label0 = QtGui.QLabel(self.configGroupBox)
        self.label0.setObjectName("label0")
        self.gridLayout_2.addWidget(self.label0, 0, 1, 1, 1)
        self.identifier_lineEdit = QtGui.QLineEdit(self.configGroupBox)
        self.identifier_lineEdit.setObjectName("identifier_lineEdit")
        self.gridLayout_2.addWidget(self.identifier_lineEdit, 0, 2, 1, 2)
        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(ConfigureDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ConfigureDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ConfigureDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigureDialog)

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QtGui.QApplication.translate("ConfigureDialog", "Configure Step", None, QtGui.QApplication.UnicodeUTF8))
        self.preparedData_label.setText(QtGui.QApplication.translate("ConfigureDialog", "Prepared data:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.preparedData_pushButton.setText(QtGui.QApplication.translate("ConfigureDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label0.setText(QtGui.QApplication.translate("ConfigureDialog", "Identifier:  ", None, QtGui.QApplication.UnicodeUTF8))

