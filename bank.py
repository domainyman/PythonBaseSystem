# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bank.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_bank(object):
    def setupUi(self, bank):
        bank.setObjectName("bank")
        bank.resize(522, 272)
        self.textBrowser = QtWidgets.QTextBrowser(bank)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 501, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.widget = QtWidgets.QWidget(bank)
        self.widget.setGeometry(QtCore.QRect(20, 70, 491, 141))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ac_na_ed = QtWidgets.QLineEdit(self.widget)
        self.ac_na_ed.setObjectName("ac_na_ed")
        self.horizontalLayout.addWidget(self.ac_na_ed)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.bank_cod_ed = QtWidgets.QLineEdit(self.widget)
        self.bank_cod_ed.setObjectName("bank_cod_ed")
        self.horizontalLayout_2.addWidget(self.bank_cod_ed)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.bank_acc_ed = QtWidgets.QLineEdit(self.widget)
        self.bank_acc_ed.setObjectName("bank_acc_ed")
        self.horizontalLayout_3.addWidget(self.bank_acc_ed)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.widget1 = QtWidgets.QWidget(bank)
        self.widget1.setGeometry(QtCore.QRect(307, 230, 201, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.quit_bu = QtWidgets.QPushButton(self.widget1)
        self.quit_bu.setObjectName("quit_bu")
        self.horizontalLayout_4.addWidget(self.quit_bu)

        self.retranslateUi(bank)
        self.quit_bu.clicked.connect(bank.close)
        QtCore.QMetaObject.connectSlotsByName(bank)

    def retranslateUi(self, bank):
        _translate = QtCore.QCoreApplication.translate
        bank.setWindowTitle(_translate("bank", "Form"))
        self.textBrowser.setHtml(_translate("bank", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">Bank Info</span></p></body></html>"))
        self.label.setText(_translate("bank", "Account Name: "))
        self.label_2.setText(_translate("bank", "Bank Code & Branch Code: "))
        self.label_3.setText(_translate("bank", "Account No.:"))
        self.pushButton.setText(_translate("bank", "Upload"))
        self.quit_bu.setText(_translate("bank", "Quit"))
