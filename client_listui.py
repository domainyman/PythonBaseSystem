# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_listui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_client_list(object):
    def setupUi(self, client_list):
        client_list.setObjectName("client_list")
        client_list.resize(700, 500)
        client_list.setMinimumSize(QtCore.QSize(700, 500))
        client_list.setMaximumSize(QtCore.QSize(700, 500))
        self.producteditlabel = QtWidgets.QTextBrowser(client_list)
        self.producteditlabel.setGeometry(QtCore.QRect(30, 20, 661, 51))
        self.producteditlabel.setObjectName("producteditlabel")
        self.layoutWidget = QtWidgets.QWidget(client_list)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 80, 661, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchLabel = QtWidgets.QLabel(self.layoutWidget)
        self.searchLabel.setObjectName("searchLabel")
        self.horizontalLayout.addWidget(self.searchLabel)
        self.searchLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.horizontalLayout.addWidget(self.searchLineEdit)
        self.quitbu = QtWidgets.QPushButton(self.layoutWidget)
        self.quitbu.setObjectName("quitbu")
        self.horizontalLayout.addWidget(self.quitbu)
        self.widget = QtWidgets.QWidget(client_list)
        self.widget.setGeometry(QtCore.QRect(30, 130, 661, 361))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.treeView = QtWidgets.QTreeView(self.widget)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)

        self.retranslateUi(client_list)
        self.quitbu.clicked.connect(client_list.close)
        QtCore.QMetaObject.connectSlotsByName(client_list)

    def retranslateUi(self, client_list):
        _translate = QtCore.QCoreApplication.translate
        client_list.setWindowTitle(_translate("client_list", "Form"))
        self.producteditlabel.setHtml(_translate("client_list", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; font-style:italic; text-decoration: underline;\">Client List</span></p></body></html>"))
        self.searchLabel.setText(_translate("client_list", "Search"))
        self.quitbu.setText(_translate("client_list", "Quit"))
        self.label.setText(_translate("client_list", "Dodble Click To Choose"))
