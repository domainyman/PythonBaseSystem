# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QMessageBox
from clientui import Ui_client
from connectdb import database


class Callclient(QMainWindow, Ui_client):

    def __init__(self, parent=None):
        super(Callclient, self).__init__(parent)
        self.setupUi(self)
        self.condb = database()
        self.bu_click()
        self.setupModel()
        self.search_filter()
        self.setupView()
        self.idBrowser.hide()

    def setupView(self):
        self.treeView.setModel(self.pFilterModel)
        self.treeView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.treeView.setSelectionBehavior(QAbstractItemView.SelectRows)

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
        while self.model_Model.canFetchMore():
            self.model_Model.fetchMore()

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


    def add_data(self):
        if (len(self.name_LineEdit.text())) != 0 and (len(self.ci_LineEdit.text())) != 0:
            client_na = self.name_LineEdit.text()
            client_ad = self.add_LineEdit.text()
            client_at = self.att_LineEdit.text()
            client_tel = self.tel_LineEdit.text()
            client_ci = self.ci_LineEdit.text()
            self.condb.client_add_db(client_na, client_ad, client_at, client_tel, client_ci)
            self.clear_data()
            self.model_Model.submitAll()
            self.model_Model.select()
            while self.model_Model.canFetchMore():
                self.model_Model.fetchMore()
        else:
            QMessageBox.about(self, "About", "Repeat! Please Check Data. !", )

    def get_cursor(self):
        curosor_row = self.treeView.currentIndex().row()
        contentslist = []
        for i in range(6):
            contents = self.treeView.model().data(self.treeView.model().index(curosor_row, i))
            contentslist.append(str(contents))
        print(contentslist)
        self.idBrowser.setText(contentslist[0])
        self.name_LineEdit.setText(contentslist[1])
        self.add_LineEdit.setText(contentslist[2])
        self.att_LineEdit.setText(contentslist[3])
        self.tel_LineEdit.setText(contentslist[4])
        self.ci_LineEdit.setText(contentslist[5])

    def upload_date(self):
        reply = QMessageBox.information(self, "Upload Data", "Once Upload ,Data cannot be recovered!",
                                        QMessageBox.Yes | QMessageBox.Close, QMessageBox.Close)
        if reply == QMessageBox.Yes and (len(self.name_LineEdit.text())) != 0 and (len(self.ci_LineEdit.text())) != 0:
            if (len(self.name_LineEdit.text())) != 0:
                client_na = self.name_LineEdit.text()
                client_ad = self.add_LineEdit.text()
                client_at = self.att_LineEdit.text()
                client_tel = self.tel_LineEdit.text()
                client_ci = self.ci_LineEdit.text()
                dbid = self.idBrowser.toPlainText()
                self.condb.client_updata_db(client_na, client_ad, client_at, client_tel, client_ci, dbid)
                self.model_Model.submitAll()
                self.model_Model.select()
                while self.model_Model.canFetchMore():
                    self.model_Model.fetchMore()
                self.clear_data()
        else:
            QMessageBox.about(self, "About", "Repeat! Please Check Data. !", )

    def clear_data(self):
        self.name_LineEdit.clear()
        self.add_LineEdit.clear()
        self.att_LineEdit.clear()
        self.tel_LineEdit.clear()
        self.ci_LineEdit.clear()
        self.idBrowser.clear()

    def del_data(self):
        reply = QMessageBox.information(self, "Delete Data", "Once deleted ,Data cannot be recovered!",
                                        QMessageBox.Yes | QMessageBox.Close, QMessageBox.Close)
        if reply == QMessageBox.Yes:
            if (len(self.name_LineEdit.text())) != 0:
                client_na = self.name_LineEdit.text()
                client_ad = self.add_LineEdit.text()
                self.condb.client_delpro_db(client_na, client_ad)
                self.model_Model.submitAll()
                self.model_Model.select()
                while self.model_Model.canFetchMore():
                    self.model_Model.fetchMore()
                self.clear_data()

    def bu_click(self):
        self.addbu.clicked.connect(self.add_data)
        self.Deletebu.clicked.connect(self.del_data)
        self.treeView.clicked.connect(self.get_cursor)
        self.uploadbu.clicked.connect(self.upload_date)
        self.clearbu.clicked.connect(self.clear_data)

    def closeEvent(self, event):
        self.condb.closedb()
        print('window close')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Callclient()
    win.show()
    sys.exit(app.exec_())
