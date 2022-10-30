# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QInputDialog, QMessageBox
from returnui import Ui_retuennote
from callret_list import callret_list
from callcompinfo import Callcompinfo
from callclient_list import Callclient_list
from connectdb import database
from callproductedit import Callproductedit
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QDate


class Callreturn(QMainWindow, Ui_retuennote):
    def __init__(self, parent=None):
        super(Callreturn, self).__init__(parent)
        self.setupUi(self)
        self.date_lineedit.setDate(QDate.currentDate())
        self.dued_lineedit.setDate(QDate.currentDate())
        self.condb = database()
        self.inv_bu_click()
        self.le3 = QtWidgets.QLineEdit()
        self.le4 = QtWidgets.QLineEdit()
        self.le4.setText("0")
        self.search_tv_setupModel()
        self.search_tv_search_filter()
        self.search_tv_setupView()
        self.confirm_tv_setupModel()
        self.confirm_tv_setupView()
        self.inv_l_setupModel()
        self.inv_l_search_filter()
        self.inv_l_setupView()
        self.inv_l_search_filter()
        self.clear_all()

    def search_tv_setupView(self):
        self.search_tv.setModel(self.search_tv_pFilterModel)
        self.search_tv.setEnabled(False)
        self.search_tv.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.search_tv.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.search_tv.setColumnWidth(0, 40)
        self.search_tv.setColumnWidth(2, 200)
        self.search_tv.setColumnWidth(4, 50)
        self.search_tv.setColumnWidth(5, 50)
        self.search_tv.setColumnWidth(6, 50)

    def search_tv_setupModel(self):
        self.search_tv_Model = QSqlTableModel()
        self.search_tv_Model.setTable("lib")
        self.search_tv__getFieldNames()
        self.search_tv_Model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.search_tv_Model.setHeaderData(self.fldNum["id"], Qt.Horizontal, "ID")
        self.search_tv_Model.setHeaderData(self.fldNum["model"], Qt.Horizontal, "Model")
        self.search_tv_Model.setHeaderData(self.fldNum["name"], Qt.Horizontal, "Name")
        self.search_tv_Model.setHeaderData(self.fldNum["cost"], Qt.Horizontal, "Cost")
        self.search_tv_Model.setHeaderData(self.fldNum["srp"], Qt.Horizontal, "SRP")
        self.search_tv_Model.setHeaderData(self.fldNum["stock"], Qt.Horizontal, "Stock")
        self.search_tv_Model.setHeaderData(self.fldNum["rma"], Qt.Horizontal, "RMA")
        self.search_tv_Model.select()
        while self.search_tv_Model.canFetchMore():
            self.search_tv_Model.fetchMore()

    def search_tv_search_filter(self):
        self.search_tv_pFilterModel = QSortFilterProxyModel()
        self.pdsearch__lineedit.setPlaceholderText("Search here")
        self.search_tv_pFilterModel.setSourceModel(self.search_tv_Model)
        self.search_tv_pFilterModel.setFilterKeyColumn(-1)
        self.search_tv_pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pdsearch__lineedit.textChanged.connect(self.search_tv_pFilterModel.setFilterRegExp)

    def search_tv__getFieldNames(self):
        self.emptyRec = self.search_tv_Model.record()
        self.fldNum = {}
        for i in range(self.emptyRec.count()):
            fieldName = self.emptyRec.fieldName(i)
            self.fldNum.setdefault(fieldName)
            self.fldNum[fieldName] = i

    def confirm_tv_setupView(self):
        self.confirm_tv.setModel(self.confirm_tvModel)
        self.confirm_tv.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.confirm_tv.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.confirm_tv.setColumnWidth(0, 40)
        self.confirm_tv.setColumnWidth(1, 80)
        self.confirm_tv.setColumnWidth(2, 100)
        self.confirm_tv.setColumnWidth(3, 200)
        self.confirm_tv.setColumnWidth(4, 80)
        self.confirm_tv.setColumnWidth(5, 80)

    def confirm_tv_setupModel(self):
        self.confirm_tvModel = QSqlTableModel()
        self.confirm_tvModel.setTable("ret_item_tmp")
        self.confirm_tvModel.setHeaderData(0, Qt.Horizontal, "ID")
        self.confirm_tvModel.setHeaderData(1, Qt.Horizontal, "Invoice No")
        self.confirm_tvModel.setHeaderData(2, Qt.Horizontal, "Model")
        self.confirm_tvModel.setHeaderData(3, Qt.Horizontal, "Name")
        self.confirm_tvModel.setHeaderData(4, Qt.Horizontal, "Price")
        self.confirm_tvModel.setHeaderData(5, Qt.Horizontal, "QTY")
        self.confirm_tvModel.select()
        while self.confirm_tvModel.canFetchMore():
            self.confirm_tvModel.fetchMore()

    def inv_add_data(self):

        if ((len(self.inv_lineedit.text())) != 0 and (len(self.billtolineedit.text())) != 0 and (
        len(self.address_lineedit.text())) != 0
                and (len(self.cusid_lineedit.text())) != 0 and (self.confirm_tvModel.rowCount() > 0)):
            reply = QMessageBox.information(self, "Add Return Note", "Add Return Note ? ",
                                            QMessageBox.Yes | QMessageBox.Close, QMessageBox.Close)
            if reply == QMessageBox.Yes:
                iv = self.inv_lineedit.text()
                da = self.date_lineedit.text()
                bi = self.billtolineedit.text()
                ad = self.address_lineedit.text()
                at = self.attn_lineedit.text()
                te = self.tel__lineedit.text()
                cia = self.cusid_lineedit.text()
                ci = cia.upper()
                self.cusid_lineedit.setText(ci)
                du = self.dued_lineedit.text()
                sa = self.sales_lineedit.text()
                sl = self.salestel_lineedit.text()
                c1 = self.cm1_lineedit.text()
                c2 = self.cm2_lineedit.text()
                c3 = self.cm3_lineedit.text()
                to_am = self.total_ed.text()
                self.checkinfo = self.condb.check_retnum(iv)
                if (iv in self.checkinfo) is False:
                    self.condb.ret_add_db_p1(iv, da, bi, ad, at, te, ci, du, sa, sl, c1, c2, c3, to_am)
                    self.cap = self.condb.retcapselect_db()
                    self.exc_res = self.condb.excision_results(self.cap,5)
                    self.stock_iv,self.res = self.condb.upload_all_prod_ret(self.exc_res)
                    self.condb.upl_retprodqty(self.res)
                else:
                    QMessageBox.about(self, "About", "Repeat! Please Check NO./PI. !", )
                    self.condb.del_ret_table()
                    self.confirm_tvModel.select()
                    while self.confirm_tvModel.canFetchMore():
                        self.confirm_tvModel.fetchMore()
                self.clear_all()
        else:
            QMessageBox.about(self, "About", "Please Enter Info Correctly!", )

    def checkBoxChangedAction(self, state):
        if state == Qt.Checked:
            self.checkinfo = self.condb.check_invnum(self.inv_lineedit.text())
            if (self.inv_lineedit.text() in self.checkinfo) is True:
                QMessageBox.about(self, "About", "Repeat! Please Check NO./PI. !", )
                self.inv_lineedit.setEnabled(True)
                self.date_lineedit.setEnabled(True)
                self.billtolineedit.setEnabled(True)
                self.address_lineedit.setEnabled(True)
                self.attn_lineedit.setEnabled(True)
                self.tel__lineedit.setEnabled(True)
                self.cusid_lineedit.setEnabled(True)
                self.dued_lineedit.setEnabled(True)
                self.sales_lineedit.setEnabled(True)
                self.salestel_lineedit.setEnabled(True)
                self.cm1_lineedit.setEnabled(True)
                self.cm2_lineedit.setEnabled(True)
                self.cm3_lineedit.setEnabled(True)
                self.search_tv.setEnabled(False)
            elif (self.inv_lineedit.text() in self.checkinfo) is False:
                self.inv_lineedit.setEnabled(False)
                self.date_lineedit.setEnabled(False)
                self.billtolineedit.setEnabled(False)
                self.address_lineedit.setEnabled(False)
                self.attn_lineedit.setEnabled(False)
                self.tel__lineedit.setEnabled(False)
                self.cusid_lineedit.setEnabled(False)
                self.dued_lineedit.setEnabled(False)
                self.sales_lineedit.setEnabled(False)
                self.salestel_lineedit.setEnabled(False)
                self.cm1_lineedit.setEnabled(False)
                self.cm2_lineedit.setEnabled(False)
                self.cm3_lineedit.setEnabled(False)
                if (len(self.inv_lineedit.text())) != 0:
                    self.search_tv.setEnabled(True)
                else:
                    self.search_tv.setEnabled(False)
        else:
            self.inv_lineedit.setEnabled(True)
            self.date_lineedit.setEnabled(True)
            self.billtolineedit.setEnabled(True)
            self.address_lineedit.setEnabled(True)
            self.attn_lineedit.setEnabled(True)
            self.tel__lineedit.setEnabled(True)
            self.cusid_lineedit.setEnabled(True)
            self.dued_lineedit.setEnabled(True)
            self.sales_lineedit.setEnabled(True)
            self.salestel_lineedit.setEnabled(True)
            self.cm1_lineedit.setEnabled(True)
            self.cm2_lineedit.setEnabled(True)
            self.cm3_lineedit.setEnabled(True)
            self.search_tv.setEnabled(False)

    def toconfirm(self):
        tocf_list = []
        toconfirm_row = self.search_tv.currentIndex().row()
        print(toconfirm_row)
        for i in range(7):
            confirm = self.search_tv.model().data(self.search_tv.model().index(toconfirm_row, i))
            tocf_list.append(str(confirm))
        print(tocf_list)
        iv = self.inv_lineedit.text()
        mod = tocf_list[1]
        nam = tocf_list[2]
        if self.inv_rma_cbox.currentText() == "SRP":
            self.getsrp_int()
            pri = self.le4.text()
        else:
            pri = tocf_list[4]
        pcs = self.le3.text()
        self.ret_tmpcount = self.condb.ret_tmpco()
        if self.ret_tmpcount < 20:
            self.condb.ret_toconfirm_db(iv, mod, nam, pri, pcs)
            self.condb.commitdb()
            self.tot_am()
        else:
            QMessageBox.about(self, "About", "Over 20 items", )
        self.search_tv_Model.select()
        while self.search_tv_Model.canFetchMore():
            self.search_tv_Model.fetchMore()

    def getsrp_int(self):
        num, ok = QInputDialog.getInt(self, "Please enter SRP", "Please enter SRP", 0, 0, 2147483647, 1)
        if ok:
            self.le4.setText(str(num))

    def getcomf_int(self):
        num, ok = QInputDialog.getInt(self, "Please enter QTY", "Please enter QTY", 0, 1, 1000, 1)
        if ok:
            self.le3.setText(str(num))
            self.toconfirm()
            self.confirm_tvModel.select()
            while self.confirm_tvModel.canFetchMore():
                self.confirm_tvModel.fetchMore()

    def delcon_data(self):
        curosor_row = self.confirm_tv.currentIndex().row()
        contentslist = []
        contents = self.confirm_tv.model().data(self.confirm_tv.model().index(curosor_row, 2))
        contentslist.append(str(contents))
        contents = self.confirm_tv.model().data(self.confirm_tv.model().index(curosor_row, 0))
        contentslist.append(str(contents))
        na = contentslist[0]
        id = contentslist[1]
        self.condb.del_ret_conf_db(na, id)
        self.tot_am()
        self.confirm_tvModel.submitAll()
        self.confirm_tvModel.select()
        while self.confirm_tvModel.canFetchMore():
            self.confirm_tvModel.fetchMore()

    def clear_invdata(self):
        self.inv_lineedit.clear()
        self.billtolineedit.clear()
        self.address_lineedit.clear()
        self.attn_lineedit.clear()
        self.tel__lineedit.clear()
        self.cusid_lineedit.clear()
        self.sales_lineedit.clear()
        self.salestel_lineedit.clear()
        self.cm1_lineedit.clear()
        self.cm2_lineedit.clear()
        self.cm3_lineedit.clear()
        self.total_ed.clear()

    def inv_l_setupView(self):
        self.inv_list_view.setModel(self.inv_l_pFilterModel)
        self.inv_list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.inv_list_view.verticalHeader().hide()
        self.inv_list_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.inv_list_view.setSortingEnabled(True)
        self.inv_list_view.setColumnWidth(1, 170)
        self.inv_list_view.setColumnHidden(0, True)
        for x in range(2, 96):
            self.inv_list_view.setColumnHidden(x, True)

    def inv_l_setupModel(self):
        self.inv_l_Model = QSqlTableModel()
        self.inv_l_Model.setTable("return")
        self.inv_l_Model.setHeaderData(1, Qt.Horizontal, "Return No")
        self.inv_l_Model.select()
        while self.inv_l_Model.canFetchMore():
            self.inv_l_Model.fetchMore()

    def get_inv_cursor(self):
        self.inv_contentslist = []
        self.inv_curosor_row = self.inv_list_view.currentIndex().row()
        for i in range(95):
            contents = self.inv_list_view.model().data(self.inv_list_view.model().index(self.inv_curosor_row, i))
            self.inv_contentslist.append(str(contents))
        return self.inv_contentslist

    def inv_l_search_filter(self):
        self.inv_l_pFilterModel = QSortFilterProxyModel()
        print('Connect search_filter ok')
        self.inv_sear_ed.setPlaceholderText("Search here")
        self.inv_l_pFilterModel.setSourceModel(self.inv_l_Model)
        self.inv_l_pFilterModel.setFilterKeyColumn(1)
        self.inv_l_pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.inv_sear_ed.textChanged.connect(self.inv_l_pFilterModel.setFilterRegExp)

    def tot_am(self):
        total = self.condb.rettot_am()
        print(total)
        self.total_ed.setText(str(total))

    def check_no(self):
        inva = self.inv_lineedit.text()
        inv = inva.upper()
        self.inv_lineedit.setText(inv)
        self.checkinfo = self.condb.check_retnum(inv)
        if (inv in self.checkinfo) is True:
            QMessageBox.about(self, "About", "Repeat! Please Check NO./PI. !", )
            self.inv_lineedit.clear()

        if (inv in self.checkinfo) is False:
            pass

    def inv_bu_click(self):
        self.enter.clicked.connect(self.inv_add_data)
        self.Lock_cb.stateChanged.connect(self.checkBoxChangedAction)
        self.search_tv.clicked.connect(self.getcomf_int)
        self.confirm_tv.clicked.connect(self.delcon_data)
        self.clear.clicked.connect(self.clear_all)
        self.inv_list_view.clicked.connect(self.c_invstat)
        self.companyinfo.clicked.connect(self.c_compinfo)
        self.client.clicked.connect(self.c_client_list)
        self.proded_bu.clicked.connect(self.c_proded_list)
        self.inv_lineedit.editingFinished.connect(self.check_no)

    def c_compinfo(self):
        self.call_cominfo = Callcompinfo()
        self.call_cominfo.show()

    def c_invstat(self):
        self.info = self.get_inv_cursor()
        self.call_invstat = callret_list(self.info)
        self.call_invstat.my_Signal.connect(self.clear_all)
        self.call_invstat.show()

    def c_client_list(self):
        self.call_client_list = Callclient_list()
        self.call_client_list.my_Signal.connect(self.client_listshow)
        self.call_client_list.show()

    def c_proded_list(self):
        self.call_proded_list = Callproductedit()
        self.call_proded_list.my_Signal.connect(self.ref)
        self.call_proded_list.show()

    def ref(self):
        self.search_tv_Model.select()
        while self.search_tv_Model.canFetchMore():
            self.search_tv_Model.fetchMore()

    def client_listshow(self, val):
        contentslist = val
        self.billtolineedit.setText(contentslist[1])
        self.address_lineedit.setText(contentslist[2])
        self.attn_lineedit.setText(contentslist[3])
        self.tel__lineedit.setText(contentslist[4])
        self.cusid_lineedit.setText(contentslist[5])

    def clear_all(self):
        self.clear_invdata()
        self.condb.del_ret_table()
        self.search_tv.setEnabled(False)
        self.Lock_cb.setChecked(False)
        self.confirm_tvModel.select()
        while self.confirm_tvModel.canFetchMore():
            self.confirm_tvModel.fetchMore()
        self.inv_l_Model.select()
        while self.inv_l_Model.canFetchMore():
            self.inv_l_Model.fetchMore()
        self.search_tv_Model.select()
        while self.search_tv_Model.canFetchMore():
            self.search_tv_Model.fetchMore()

    def closeEvent(self, event):
        self.clear_all()
        self.condb.closedb()
        print('window close')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Callreturn()
    win.show()
    sys.exit(app.exec_())
