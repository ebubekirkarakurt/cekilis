# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ebuka\Desktop\otomasyonprojesi\form2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(968, 622)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 80, 921, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 30, 251, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 520, 771, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tamamButton = QtWidgets.QPushButton(Form)
        self.tamamButton.setGeometry(QtCore.QRect(830, 560, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tamamButton.setFont(font)
        self.tamamButton.setObjectName("tamamButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(200, 560, 541, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 560, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Kazananlar"))
        self.label.setText(_translate("Form", "Kazananların Listesi"))
        self.label_2.setText(_translate("Form", "Kazanan vatandaşlarımızla en kısa zamanda irtibata geçilecektir.."))
        self.tamamButton.setText(_translate("Form", "Teşekkürler"))
        self.label_3.setText(_translate("Form", "%15 Şehit Yakınları, %10 Emekli, %10 Engel Durumu Olanlar, %65 Özel Durumu Olmayanlar"))
        self.label_4.setText(_translate("Form", "Çekiliş Dağılım Oranları:"))
