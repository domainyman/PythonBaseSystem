# -*- coding: utf-8 -*-

import sys

from PyQt5.QtGui import QDoubleValidator, QIntValidator
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QMessageBox, QCompleter
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QDate
from purchaseui import Ui_purchase
from callpur_list import callpur_list
from connectdb import database


class Callpurchase(QMainWindow, Ui_purchase):
    def __init__(self, parent=None):
        super(Callpurchase, self).__init__(parent)
        self.setupUi(self)
        self.condb = database()
        self.purlist = self.condb.pur_sup_list()
        completer = QCompleter(self.purlist)
        self.supplier_edit.setCompleter(completer)
        dbl_validator = QDoubleValidator(self)
        dbl_validator.setNotation(QDoubleValidator.StandardNotation)
        dbl_validator.setDecimals(6)
        int_validator = QIntValidator(self)
        int_validator.setRange(0, 9999999)
        self.purprice_ed.setValidator(dbl_validator)
        self.purqty_ed.setValidator(int_validator)
        self.date_lineedit.setDate(QDate.currentDate())
        self.search_tv_setupModel()
        self.search_tv_search_filter()
        self.search_tv_setupView()
        self.pur_confirm_tv_setupModel()
        self.pur_confirm_tv_setupView()
        self.purinv_setupModel()
        self.pur_l_search_filter()
        self.purinv_setupView()
        self.pur_bu_click()
        self.clear_purall()

    def search_tv_setupView(self):
        self.pur_search_tv.setModel(self.pur_search_tv_pFilterModel)
        self.pur_search_tv.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.pur_search_tv.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.pur_search_tv.setColumnWidth(0, 40)
        self.pur_search_tv.setEnabled(False)
        self.pur_search_tv.setColumnWidth(1, 150)
        self.pur_search_tv.setColumnWidth(2, 350)
        self.pur_search_tv.setColumnWidth(4, 50)
        self.pur_search_tv.setColumnWidth(5, 50)
        self.pur_search_tv.setColumnWidth(6, 50)

    def search_tv_setupModel(self):
        self.pur_search_tv_Model = QSqlTableModel()
        self.pur_search_tv_Model.setTable("lib")
        self.pur_search_tv__getFieldNames()
        self.pur_search_tv_Model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.pur_search_tv_Model.setHeaderData(self.fldNum["id"], Qt.Horizontal, "ID")
        self.pur_search_tv_Model.setHeaderData(self.fldNum["model"], Qt.Horizontal, "Model")
        self.pur_search_tv_Model.setHeaderData(self.fldNum["name"], Qt.Horizontal, "Name")
        self.pur_search_tv_Model.setHeaderData(self.fldNum["cost"], Qt.Horizontal, "Cost")
        self.pur_search_tv_Model.setHeaderData(self.fldNum["srp"], Qt.Horizontal, "SRP")
        self.pur_search_tv_Model.setHeaderData(self.fldNum["stock"], Qt.Horizontal, "Stock")
        self.pur_search_tv_Model.setHeaderData(self.fldNum["rma"], Qt.Horizontal, "RMA")
        self.pur_search_tv_Model.select()
        while self.pur_search_tv_Model.canFetchMore():
            self.pur_search_tv_Model.fetchMore()

    def search_tv_search_filter(self):
        self.pur_search_tv_pFilterModel = QSortFilterProxyModel()
        self.pdsearch__lineedit.setPlaceholderText("Search here")
        self.pur_search_tv_pFilterModel.setSourceModel(self.pur_search_tv_Model)
        self.pur_search_tv_pFilterModel.setFilterKeyColumn(-1)
        self.pur_search_tv_pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pdsearch__lineedit.textChanged.connect(self.pur_search_tv_pFilterModel.setFilterRegExp)

    def pur_search_tv__getFieldNames(self):
        self.emptyRec = self.pur_search_tv_Model.record()
        self.fldNum = {}
        for i in range(self.emptyRec.count()):
            fieldName = self.emptyRec.fieldName(i)
            self.fldNum.setdefault(fieldName)
            self.fldNum[fieldName] = i

    def pur_confirm_tv_setupView(self):
        self.pur_confirm_tv.setModel(self.pur_confirm_tvModel)
        self.pur_confirm_tv.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.pur_confirm_tv.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.pur_confirm_tv.setColumnWidth(0, 40)
        self.pur_confirm_tv.setColumnWidth(1, 150)
        self.pur_confirm_tv.setColumnWidth(2, 350)
        self.pur_confirm_tv.setColumnWidth(4, 50)
        self.pur_confirm_tv.setColumnWidth(5, 50)
        self.pur_confirm_tv.setColumnWidth(6, 50)

    def pur_confirm_tv_setupModel(self):
        self.pur_confirm_tvModel = QSqlTableModel()
        self.pur_confirm_tvModel.setTable("purchase_tmp")
        self.pur_confirm_tvModel.setHeaderData(0, Qt.Horizontal, "ID")
        self.pur_confirm_tvModel.setHeaderData(1, Qt.Horizontal, "No.")
        self.pur_confirm_tvModel.setHeaderData(2, Qt.Horizontal, "Name")
        self.pur_confirm_tvModel.setHeaderData(3, Qt.Horizontal, "Price")
        self.pur_confirm_tvModel.setHeaderData(4, Qt.Horizontal, "QTY")
        self.pur_confirm_tvModel.select()
        while self.pur_confirm_tvModel.canFetchMore():
            self.pur_confirm_tvModel.fetchMore()

    def pur_get_cursor(self):
        pur_curosor_row = self.pur_search_tv.currentIndex().row()
        self.pur_itemlist = []
        for i in range(7):
            contents = self.pur_search_tv.model().data(self.pur_search_tv.model().index(pur_curosor_row, i))
            self.pur_itemlist.append(str(contents))
        self.purname_ed.setText(self.pur_itemlist[2])
        self.purprice_ed.setText(self.pur_itemlist[3])

    def pur_toconfirm(self):
        if ((len(self.no_edit.text()) != 0) and (len(self.purqty_ed.text()) != 0)):
            iv = self.no_edit.text()
            p_n = self.purname_ed.text()
            p_p = self.purprice_ed.text()
            p_qty = self.purqty_ed.text()
            self.pur_tmpcount = self.condb.pur_tmpco()
            if self.pur_tmpcount < 20:
                self.condb.pur_toconfirm_db(iv, p_n, p_p, p_qty)
                self.totpur_am()
                self.pur_clear()
            else:
                QMessageBox.about(self, "About", "Over 20 items", )
            self.pur_confirm_tvModel.submitAll()
            self.pur_confirm_tvModel.select()
            while self.pur_confirm_tvModel.canFetchMore():
                self.pur_confirm_tvModel.fetchMore()

    def pur_add_data(self):
        if ((len(self.no_edit.text())) != 0 and (len(self.supplier_edit.text())) != 0
                and (self.pur_confirm_tvModel.rowCount() > 0)):
            reply = QMessageBox.information(self, "Add Purchase", "Add Purchase ? ",
                                            QMessageBox.Yes | QMessageBox.Close, QMessageBox.Close)
            if reply == QMessageBox.Yes:
                nu_no = self.no_edit.text()
                da = self.date_lineedit.text()
                supa = self.supplier_edit.text()
                sup = supa.upper()
                self.supplier_edit.setText(sup)
                amount = self.to_am_edit.text()
                qty = self.to_qty_edit.text()
                self.checkinfo = self.condb.check_purnum(nu_no)
                print(self.checkinfo)
                print(nu_no in self.checkinfo)
                if (nu_no in self.checkinfo) is False:
                    self.condb.pur_adddb(nu_no, da, sup, amount, qty)
                    self.cap = self.condb.pur_capselect_db()
                    self.exc_res = self.condb.excision_results(self.cap,4)
                    self.stock_iv,self.res = self.condb.upload_all_prod_pur(self.exc_res)
                    self.condb.upl_purdqty(self.res)
                else:
                    QMessageBox.about(self, "About", "Repeat! Please Check NO./PI. !", )
                    self.condb.del_pur_table()
                    self.pur_confirm_tvModel.select()
                    while self.pur_confirm_tvModel.canFetchMore():
                        self.pur_confirm_tvModel.fetchMore()
                self.clear_purall()
        else:
            QMessageBox.about(self, "About", "Please Enter Info Correctly!", )

    def pur_delcon_data(self):
        curosor_row = self.pur_confirm_tv.currentIndex().row()
        contentslist = []
        contents = self.pur_confirm_tv.model().data(self.pur_confirm_tv.model().index(curosor_row, 2))
        contentslist.append(str(contents))
        na = contentslist[0]
        self.condb.del_pur_conf_db(na)
        self.totpur_am()
        self.pur_confirm_tvModel.submitAll()
        self.pur_confirm_tvModel.select()
        while self.pur_confirm_tvModel.canFetchMore():
            self.pur_confirm_tvModel.fetchMore()

    def pur_clear(self):
        self.purname_ed.clear()
        self.purprice_ed.clear()
        self.purqty_ed.clear()

    def pur_clearp2(self):
        self.no_edit.clear()
        self.supplier_edit.clear()
        self.to_am_edit.clear()
        self.to_qty_edit.clear()

    def clear_purall(self):
        self.pur_clear()
        self.pur_clearp2()
        self.condb.del_pur_table()
        self.pur_search_tv.setEnabled(False)
        self.Lock_cb.setChecked(False)
        self.pur_search_tv_Model.select()
        while self.pur_search_tv_Model.canFetchMore():
            self.pur_search_tv_Model.fetchMore()
        self.pur_confirm_tvModel.select()
        while self.pur_confirm_tvModel.canFetchMore():
            self.pur_confirm_tvModel.fetchMore()
        self.pur_l_Model.select()
        while self.pur_l_Model.canFetchMore():
            self.pur_l_Model.fetchMore()

    def checkBoxChangedAction(self, state):
        if state == Qt.Checked:
            self.checkinfo = self.condb.check_purnum(self.no_edit.text())
            if (self.no_edit.text() in self.checkinfo) is True:
                QMessageBox.about(self, "About", "Repeat! Please Check NO./PI. !", )
                self.no_edit.setEnabled(True)
                self.date_lineedit.setEnabled(True)
                self.supplier_edit.setEnabled(True)
                self.pur_search_tv.setEnabled(False)
            elif (self.no_edit.text() in self.checkinfo) is False:
                self.no_edit.setEnabled(False)
                self.date_lineedit.setEnabled(False)
                self.supplier_edit.setEnabled(False)
                if (len(self.no_edit.text())) != 0 and (len(self.supplier_edit.text())) != 0:
                    self.pur_search_tv.setEnabled(True)
                else:
                    self.pur_search_tv.setEnabled(False)
        else:
            self.no_edit.setEnabled(True)
            self.date_lineedit.setEnabled(True)
            self.supplier_edit.setEnabled(True)

    def purinv_setupView(self):
        self.pur_list_view.setModel(self.pur_l_pFilterModel)
        self.pur_list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.pur_list_view.verticalHeader().hide()
        self.pur_list_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.pur_list_view.setSortingEnabled(True)
        self.pur_list_view.setColumnWidth(1, 140)
        self.pur_list_view.setColumnHidden(0, True)
        for x in range(2, 66):
            self.pur_list_view.setColumnHidden(x, True)

    def purinv_setupModel(self):
        self.pur_l_Model = QSqlTableModel()
        self.pur_l_Model.setTable("purchase")
        self.pur_l_Model.setHeaderData(1, Qt.Horizontal, "Purchase No")
        self.pur_l_Model.select()
        while self.pur_l_Model.canFetchMore():
            self.pur_l_Model.fetchMore()

    def get_pur_cursor(self):
        self.pur_contentslist = []
        self.pur_curosor_row = self.pur_list_view.currentIndex().row()
        for i in range(66):
            contents = self.pur_list_view.model().data(self.pur_list_view.model().index(self.pur_curosor_row, i))
            self.pur_contentslist.append(str(contents))
        return self.pur_contentslist

    def pur_l_search_filter(self):
        self.pur_l_pFilterModel = QSortFilterProxyModel()
        self.pur_sear_ed.setPlaceholderText("Search here")
        self.pur_l_pFilterModel.setSourceModel(self.pur_l_Model)
        self.pur_l_pFilterModel.setFilterKeyColumn(1)
        self.pur_l_pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pur_sear_ed.textChanged.connect(self.pur_l_pFilterModel.setFilterRegExp)

    def c_pur_list(self):
        self.info = self.get_pur_cursor()
        self.call_pur_list = callpur_list(self.info)
        self.call_pur_list.my_Signal.connect(self.clear_purall)
        self.call_pur_list.show()

    def totpur_am(self):
        total = self.condb.tot_pur_am()
        totalqty = self.condb.tot_pur_qty()
        self.to_am_edit.setText(str(total))
        self.to_qty_edit.setText(str(totalqty))

    def check_no(self):
        inva = self.no_edit.text()
        inv = inva.upper()
        self.no_edit.setText(inv)
        self.checkinfo = self.condb.check_purnum(inv)
        print(inv in self.checkinfo)
        if (inv in self.checkinfo) is True:
            QMessageBox.about(self, "About", "Repeat! Please Check NO./PI. !", )
            self.no_edit.clear()

        if (inv in self.checkinfo) is False:
            pass

    def upper(self):
        self.supplier_edit.setText(self.supplier_edit.text().upper())

    def pur_bu_click(self):
        self.pur_search_tv.clicked.connect(self.pur_get_cursor)
        self.enter_bu.clicked.connect(self.pur_toconfirm)
        self.clear.clicked.connect(self.clear_purall)
        self.pur_confirm_tv.clicked.connect(self.pur_delcon_data)
        self.pur_list_view.clicked.connect(self.c_pur_list)
        self.enter.clicked.connect(self.pur_add_data)
        self.Lock_cb.stateChanged.connect(self.checkBoxChangedAction)
        self.no_edit.editingFinished.connect(self.check_no)
        self.supplier_edit.textChanged.connect(self.upper)

    def closeEvent(self, event):
        self.clear_purall()
        self.condb.closedb()
        print('window close')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Callpurchase()
    win.show()
    sys.exit(app.exec_())
