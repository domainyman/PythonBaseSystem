# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractItemView
from client_listui import Ui_client_list
from connectdb import database


class Callclient_list(QMainWindow, Ui_client_list):
    my_Signal = QtCore.pyqtSignal(list)

    def __init__(self, parent=None):
        super(Callclient_list, self).__init__(parent)
        self.setupUi(self)
        self.condb = database()
        self.bu_click()
        self.setupModel()
        self.search_filter()
        self.setupView()

    def setupView(self):
        self.treeView.setModel(self.pFilterModel)
        self.treeView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.treeView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.treeView.setColumnWidth(0, 40)
        self.treeView.setColumnWidth(1, 150)
        self.treeView.setColumnWidth(2, 250)
        self.treeView.setColumnWidth(3, 70)
        self.treeView.setColumnWidth(4, 70)
        self.treeView.setColumnWidth(5, 70)

    def setupModel(self):
        self.model_Model = QSqlTableModel()
        self.model_Model.setTable("client")
        self.__getFieldNames()
        self.model_Model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model_Model.setHeaderData(self.fldNum["id"], Qt.Horizontal, "ID")
        self.model_Model.setHeaderData(self.fldNum["name"], Qt.Horizontal, "Name")
        self.model_Model.setHeaderData(self.fldNum["ad"], Qt.Horizontal, "Address")
        self.model_Model.setHeaderData(self.fldNum["at"], Qt.Horizontal, "Attn")
        self.model_Model.setHeaderData(self.fldNum["tel"], Qt.Horizontal, "Tel")
        self.model_Model.setHeaderData(self.fldNum["ci"], Qt.Horizontal, "Customer ID")
        self.model_Model.select()

    def search_filter(self):
        self.pFilterModel = QSortFilterProxyModel()
        self.searchLineEdit.setPlaceholderText("Search here")
        self.pFilterModel.setSourceModel(self.model_Model)
        self.pFilterModel.setFilterKeyColumn(1)
        self.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.searchLineEdit.textChanged.connect(self.pFilterModel.setFilterRegExp)

    def __getFieldNames(self):
        self.emptyRec = self.model_Model.record()
        self.fldNum = {}
        for i in range(self.emptyRec.count()):
            fieldName = self.emptyRec.fieldName(i)
            self.fldNum.setdefault(fieldName)
            self.fldNum[fieldName] = i

    def get_cursor(self):
        curosor_row = self.treeView.currentIndex().row()
        print(curosor_row)
        contentslist = []
        for i in range(6):
            contents = self.treeView.model().data(self.treeView.model().index(curosor_row, i))
            contentslist.append(str(contents))
        print(contentslist)
        self.my_Signal.emit(contentslist)
        self.close()

    def bu_click(self):
        self.treeView.doubleClicked.connect(self.get_cursor)

    def closeEvent(self, event):
        self.condb.closedb()
        print('window close')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Callclient_list()
    win.show()
    sys.exit(app.exec_())
