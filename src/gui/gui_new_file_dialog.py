# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/gui/gui_new_file_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(184, 107)
        Dialog.setMaximumSize(QtCore.QSize(184, 107))
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.width_spin = QtWidgets.QSpinBox(Dialog)
        self.width_spin.setObjectName("width_spin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.width_spin)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.height_spin = QtWidgets.QSpinBox(Dialog)
        self.height_spin.setObjectName("height_spin")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.height_spin)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Set Size"))
        self.label.setText(_translate("Dialog", "Width"))
        self.label_2.setText(_translate("Dialog", "Height"))


