# -*- coding: utf-8 -*-

import sys

from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QMessageBox, QCompleter
from PyQt5.QtCore import Qt, QDate, QSortFilterProxyModel
from expenseui import Ui_expense
from callexp_list import callexp_list
from connectdb import database


class callexpense(QMainWindow, Ui_expense):
    def __init__(self, parent=None):
        super(callexpense, self).__init__(parent)
        self.condb = database()        
        dbl_validator = QDoubleValidator(self)
        dbl_validator.setNotation(QDoubleValidator.StandardNotation)
        dbl_validator.setDecimals(6)
        self.setupUi(self)
        self.explist = self.condb.exp_sup_list()
        completer = QCompleter(self.explist)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.shop_ed.setCompleter(completer)
        self.da_ed.setDate(QDate.currentDate())
        self.pri_ed.setValidator(dbl_validator)
        self.view_setupModel()
        self.view_setupView()
        self.expinv_setupModel()
        self.exp_l_search_filter()
        self.expinv_setupView()
        self.comboBox.addItems(["Shipping Fee", "Exchange", "Bank Charge", "Stationery Supplies", "Insurance",
                                "Other Expenses", "Salary and Wages", "MPF", "Rent", "Bank interest"])
        self.bu_click()
        self.clear_allexp_data()

    def comboactive(self):
        self.comb_act = self.comboBox.currentText()
        print(self.comb_act)

    def view_setupView(self):
        self.view.setModel(self.view_Model)
        self.view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.view.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.view.setColumnWidth(0, 40)
        self.view.setColumnWidth(1, 100)
        self.view.setColumnWidth(2, 250)
        self.view.setColumnWidth(3, 100)

    def view_setupModel(self):
        self.view_Model = QSqlTableModel()
        self.view_Model.setTable("expense_tmp")
        self.view_getFieldNames()
        self.view_Model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.view_Model.setHeaderData(self.fldNum["id"], Qt.Horizontal, "ID")
        self.view_Model.setHeaderData(self.fldNum["inv"], Qt.Horizontal, "No.")
        self.view_Model.setHeaderData(self.fldNum["name"], Qt.Horizontal, "Item")
        self.view_Model.setHeaderData(self.fldNum["price"], Qt.Horizontal, "Price")
        self.view_Model.select()
        while self.view_Model.canFetchMore():
            self.view_Model.fetchMore()

    def view_getFieldNames(self):
        self.emptyRec = self.view_Model.record()
        self.fldNum = {}
        for i in range(self.emptyRec.count()):
            fieldName = self.emptyRec.fieldName(i)
            self.fldNum.setdefault(fieldName)
            self.fldNum[fieldName] = i

    def upladdexp_data(self):
        if ((len(self.no_ed.text()) != 0) and (len(self.it_ed.text()) != 0) and (len(self.pri_ed.text()) != 0)):
            inv = self.no_ed.text()
            namea = self.it_ed.text()
            name = namea.upper()
            self.it_ed.setText(name)
            price = self.pri_ed.text()
            self.exp_tmpcount = self.condb.exp_tmpco()
            if self.exp_tmpcount < 10:
                self.condb.upl_exp_db(inv, name, price)
                self.tot_am()
                self.clear_addexp_data()
            else:
                QMessageBox.about(self, "About", "Over 10 items", )
            self.view_Model.submitAll()
            self.view_Model.select()
            while self.view_Model.canFetchMore():
                self.view_Model.fetchMore()

    def uplexp_db(self):
        if ((len(self.no_ed.text())) != 0 and (len(self.da_ed.text())) != 0 and (len(self.shop_ed.text())) != 0
                and (self.view_Model.rowCount() > 0)):
            reply = QMessageBox.information(self, "Add Expense", "Add Expense ? ",
                                            QMessageBox.Yes | QMessageBox.Close, QMessageBox.Close)
            if reply == QMessageBox.Yes:
                inv = self.no_ed.text()
                da = self.da_ed.text()
                sha = self.shop_ed.text()
                sh = sha.upper()
                self.shop_ed.setText(inv)
                cm = self.comboBox.currentText()
                to_am = self.am_ed.text()
                self.checkinfo = self.condb.check_expnum(inv)
                print(inv in self.checkinfo)
                if (inv in self.checkinfo) is False:
                    self.condb.upl_all_exp_db(inv, da, sh, cm, to_am)
                    self.cap = self.condb.exp_capselect_db()
                    self.exc_res = self.condb.excision_results(self.cap,3)
                    self.condb.upload_all_prod_exp(self.exc_res)
                else:
                    QMessageBox.about(self, "About", "Repeat! Please Check NO./PI. !", )
                    self.clear_allexp_data()
                self.clear_allexp_data()
        else:
            QMessageBox.about(self, "About", "Please Enter Info Correctly!", )

    def tot_am(self):
        total = self.condb.tot_exp_am()
        print(total)
        self.am_ed.setText(str(total))

    def delexp_data(self):
        curosor_row = self.view.currentIndex().row()
        print(curosor_row)
        contentslist = []
        contents = self.view.model().data(self.view.model().index(curosor_row, 2))
        contentslist.append(str(contents))
        print(contentslist)
        na = contentslist[0]
        self.condb.del_exp_db(na)
        print('Del Row')
        self.tot_am()
        self.view_Model.submitAll()
        self.view_Model.select()
        while self.view_Model.canFetchMore():
            self.view_Model.fetchMore()

    def expinv_setupView(self):
        self.tableView.setModel(self.exp_l_pFilterModel)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.verticalHeader().hide()
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setSortingEnabled(True)
        self.tableView.setColumnWidth(1, 120)
        self.tableView.setColumnHidden(0, True)
        for x in range(2, 26):
            self.tableView.setColumnHidden(x, True)

    def expinv_setupModel(self):
        self.exp_l_Model = QSqlTableModel()
        self.exp_l_Model.setTable("expense")
        self.exp_l_Model.setHeaderData(1, Qt.Horizontal, "Expense No")
        self.exp_l_Model.select()
        while self.exp_l_Model.canFetchMore():
            self.exp_l_Model.fetchMore()

    def check_no(self):
        inva = self.no_ed.text()
        inv = inva.upper()
        self.no_ed.setText(inv)
        self.checkinfo = self.condb.check_expnum(inv)
        print(self.checkinfo)
        print(inv in self.checkinfo)
        if (inv in self.checkinfo) is True:
            QMessageBox.about(self, "About", "Repeat! Please Check NO./PI. !", )
            self.it_ed.setEnabled(False)
            self.pri_ed.setEnabled(False)
            self.no_ed.clear()

        if (inv in self.checkinfo) is False:
            self.it_ed.setEnabled(True)
            self.pri_ed.setEnabled(True)

    def exp_l_search_filter(self):
        self.exp_l_pFilterModel = QSortFilterProxyModel()
        self.exp_sear_ed.setPlaceholderText("Search here")
        self.exp_l_pFilterModel.setSourceModel(self.exp_l_Model)
        self.exp_l_pFilterModel.setFilterKeyColumn(1)
        self.exp_l_pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.exp_sear_ed.textChanged.connect(self.exp_l_pFilterModel.setFilterRegExp)

    def clear_addexp_data(self):
        self.it_ed.clear()
        self.pri_ed.clear()

    def clear_allexp_data(self):
        self.clear_addexp_data()
        self.no_ed.clear()
        self.shop_ed.clear()
        self.am_ed.clear()
        self.condb.del_exp_table()
        self.view_Model.select()
        while self.view_Model.canFetchMore():
            self.view_Model.fetchMore()
        self.exp_l_Model.select()
        while self.exp_l_Model.canFetchMore():
            self.exp_l_Model.fetchMore()

    def closeEvent(self, event):
        self.condb.closedb()
        print('window close')

    def get_exp_cursor(self):
        self.exp_contentslist = []
        self.exp_curosor_row = self.tableView.currentIndex().row()
        for i in range(26):
            contents = self.tableView.model().data(self.tableView.model().index(self.exp_curosor_row, i))
            self.exp_contentslist.append(str(contents))
        return self.exp_contentslist

    def c_exp_list(self):
        self.info = self.get_exp_cursor()
        self.call_exp_list = callexp_list(self.info)
        self.call_exp_list.my_Signal.connect(self.clear_allexp_data)
        self.call_exp_list.show()


    def upper(self):
        self.shop_ed.setText(self.shop_ed.text().upper())

    def bu_click(self):
        self.view.clicked.connect(self.delexp_data)
        self.add_bu.clicked.connect(self.upladdexp_data)
        self.ent_bu.clicked.connect(self.uplexp_db)
        self.vlear_bu.clicked.connect(self.clear_allexp_data)
        self.tableView.clicked.connect(self.c_exp_list)
        self.comboBox.currentIndexChanged.connect(self.comboactive)
        self.no_ed.editingFinished.connect(self.check_no)
        self.shop_ed.textChanged.connect(self.upper)

    def closeEvent(self, event):
        self.clear_allexp_data()
        self.condb.closedb()
        print('window close')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = callexpense()
    win.show()
    sys.exit(app.exec_())
