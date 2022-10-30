# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QMessageBox
from producteditui import Ui_productedit
from connectdb import database
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtCore import Qt, QSortFilterProxyModel


class Callproductedit(QMainWindow, Ui_productedit):
    my_Signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(Callproductedit, self).__init__(parent)
        dbl_validator = QDoubleValidator(self)
        dbl_validator.setNotation(QDoubleValidator.StandardNotation)
        dbl_validator.setDecimals(6)
        self.setupUi(self)
        self.costLineEdit.setValidator(dbl_validator)
        self.srpLineEdit.setValidator(dbl_validator)
        self.condb = database()
        self.bu_click()
        self.setupModel()
        self.search_filter()
        self.setupView()
        self.amproco = self.condb.amprodco()
        self.to_amco_ed.setText(str(self.amproco))
        self.amproqty = self.condb.amprodqty()
        self.to_amqty_ed.setText(str(self.amproqty))
        self.idBrowser.hide()

    def setupView(self):
        self.treeView.setModel(self.pFilterModel)
        self.treeView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.treeView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.treeView.setColumnWidth(0, 40)
        self.treeView.setColumnWidth(2, 250)
        self.treeView.setColumnWidth(4, 50)
        self.treeView.setColumnWidth(5, 50)
        self.treeView.setColumnWidth(6, 50)

    def setupModel(self):
        self.model_Model = QSqlTableModel()
        self.model_Model.setTable("lib")
        self.__getFieldNames()
        self.model_Model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model_Model.setHeaderData(self.fldNum["id"], Qt.Horizontal, "ID")
        self.model_Model.setHeaderData(self.fldNum["model"], Qt.Horizontal, "Model")
        self.model_Model.setHeaderData(self.fldNum["name"], Qt.Horizontal, "Name")
        self.model_Model.setHeaderData(self.fldNum["cost"], Qt.Horizontal, "Cost")
        self.model_Model.setHeaderData(self.fldNum["srp"], Qt.Horizontal, "SRP")
        self.model_Model.setHeaderData(self.fldNum["stock"], Qt.Horizontal, "Stock")
        self.model_Model.setHeaderData(self.fldNum["rma"], Qt.Horizontal, "RMA")
        self.model_Model.select()
        while self.model_Model.canFetchMore():
            self.model_Model.fetchMore()

    def search_filter(self):
        self.pFilterModel = QSortFilterProxyModel()
        self.searchLineEdit.setPlaceholderText("Search here")
        self.pFilterModel.setSourceModel(self.model_Model)
        self.pFilterModel.setFilterKeyColumn(2)
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
        if (len(self.modelLineEdit.text())) != 0 and (len(self.nameLineEdit.text())) != 0:
            dbmodel = self.modelLineEdit.text()
            dbname = self.nameLineEdit.text()
            if (len(self.costLineEdit.text())) == 0:
                self.costLineEdit.setText("0")
                dbcost = self.costLineEdit.text()
            else:
                dbcost = self.costLineEdit.text()
            if (len(self.srpLineEdit.text())) == 0:
                self.srpLineEdit.setText("0")
                dbsrp = self.srpLineEdit.text()
            else:
                dbsrp = self.srpLineEdit.text()
            if (len(self.stockLineEdit.text())) == 0:
                self.stockLineEdit.setText("0")
                dbstock = self.stockLineEdit.text()
            else:
                dbstock = self.stockLineEdit.text()
            if (len(self.rmaLineEdit.text())) == 0:
                self.rmaLineEdit.setText("0")
                dbrma = self.rmaLineEdit.text()
            else:
                dbrma = self.rmaLineEdit.text()
            self.condb.add_db(dbmodel, dbname, dbcost, dbsrp, dbstock, dbrma)
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
        for i in range(7):
            contents = self.treeView.model().data(self.treeView.model().index(curosor_row, i))
            contentslist.append(str(contents))
        self.idBrowser.setText(contentslist[0])
        self.modelLineEdit.setText(contentslist[1])
        self.nameLineEdit.setText(contentslist[2])
        self.costLineEdit.setText(contentslist[3])
        self.srpLineEdit.setText(contentslist[4])
        self.stockLineEdit.setText(contentslist[5])
        self.rmaLineEdit.setText(contentslist[6])

    def upload_date(self):
        reply = QMessageBox.information(self, "Upload Data", "Once Upload ,Data cannot be recovered!",
                                        QMessageBox.Yes | QMessageBox.Close, QMessageBox.Close)
        if reply == QMessageBox.Yes and (len(self.modelLineEdit.text())) != 0 and (len(self.nameLineEdit.text())) != 0:
            if (len(self.modelLineEdit.text())) != 0:
                dbmodel = self.modelLineEdit.text()
                dbname = self.nameLineEdit.text()
                dbcost = self.costLineEdit.text()
                dbsrp = self.srpLineEdit.text()
                dbstock = self.stockLineEdit.text()
                dbrma = self.rmaLineEdit.text()
                dbid = self.idBrowser.toPlainText()
                self.condb.updata_db(dbmodel, dbname, dbcost, dbsrp, dbstock, dbrma, dbid)
                self.clear_data()
                self.model_Model.submitAll()
                self.model_Model.select()
                while self.model_Model.canFetchMore():
                    self.model_Model.fetchMore()                
        else:
            QMessageBox.about(self, "About", "Repeat! Please Check Data. !", )

    def clear_data(self):
        self.modelLineEdit.clear()
        self.nameLineEdit.clear()
        self.costLineEdit.clear()
        self.srpLineEdit.clear()
        self.stockLineEdit.clear()
        self.rmaLineEdit.clear()
        self.idBrowser.clear()

    def del_data(self):
        reply = QMessageBox.information(self, "Delete Data", "Once deleted ,Data cannot be recovered!",
                                        QMessageBox.Yes | QMessageBox.Close, QMessageBox.Close)
        if reply == QMessageBox.Yes:
            if (len(self.modelLineEdit.text())) != 0 and int(self.stockLineEdit.text()) == 0:
                dbmodel = self.modelLineEdit.text()
                dbname = self.nameLineEdit.text()
                self.condb.delpro_db(dbmodel, dbname)
                self.model_Model.submitAll()
                self.model_Model.select()
                while self.model_Model.canFetchMore():
                    self.model_Model.fetchMore()
                self.clear_data()
            else:
                QMessageBox.about(self, "About", "Repeat!Product Have Stock. !", )

    def bu_click(self):
        self.addbu.clicked.connect(self.add_data)
        self.Deletebu.clicked.connect(self.del_data)
        self.treeView.clicked.connect(self.get_cursor)
        self.uploadbu.clicked.connect(self.upload_date)
        self.clearbu.clicked.connect(self.clear_data)

    def sendEditContent(self):
        self.my_Signal.emit()

    def closeEvent(self, event):
        self.sendEditContent()
        self.condb.closedb()
        print('window close')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Callproductedit()
    win.show()
    sys.exit(app.exec_())
