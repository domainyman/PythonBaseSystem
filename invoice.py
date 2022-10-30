# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QInputDialog, QMessageBox
from invoiceui import Ui_invoice
from callinv_list import callinv_list
from callcompinfo import Callcompinfo
from callclient_list import Callclient_list
from connectdb import database
from callproductedit import Callproductedit
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QDate


class Callinvoice(QMainWindow, Ui_invoice):
    def __init__(self, parent=None):
        super(Callinvoice, self).__init__(parent)
        self.setupUi(self)
        self.date_lineedit.setDate(QDate.currentDate())
        self.dued_lineedit.setDate(QDate.currentDate())
        self.condb = database()
        self.inv_bu_click()
        self.search_tv_setupModel()
        self.search_tv_search_filter()
        self.search_tv_setupView()
        self.confirm_tv_setupModel()
        self.confirm_tv_setupView()
        self.inv_l_setupModel()
        self.inv_l_search_filter()
        self.inv_l_setupView()
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
        self.search_tv.setColumnHidden(7,True)

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
        self.confirm_tvModel.setTable("inv_item_tmp")
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
        if ((len(self.inv_lineedit.text())) != 0 and (len(self.billtolineedit.text()))!= 0 and (
        len(self.address_lineedit.text())) != 0
                and (len(self.cusid_lineedit.text())) != 0 and (self.confirm_tvModel.rowCount() > 0)):
            reply = QMessageBox.information(self, "Add INVOICE", "Add Invoice ? ",
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
                self.checkinfo = self.condb.check_invnum(iv)
                if (iv in self.checkinfo) is False:
                    self.condb.inv_add_db_p1(iv, da, bi, ad, at, te, ci, du, sa, sl, c1, c2, c3, to_am)
                    self.cap = self.condb.capselect_db()
                    self.exc_res = self.condb.excision_results(self.cap,5)
                    self.stock_iv,self.res = self.condb.upload_all_prod_inv(self.exc_res)
                    self.condb.upl_prodqty(self.res)
                else:
                    QMessageBox.about(self, "About", "Repeat! Please Check NO./PI. !", )
                    self.condb.del_table()
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
                if (len(self.inv_lineedit.text()) != 0):
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

    def getcomf_int(self):
        if (len(self.inv_lineedit.text()) != 0):
            self.iv = self.inv_lineedit.text()
            self.confirm_data = self.toconfirm()
            self.inv_tmpcount = self.condb.inv_tmpco()
            if (self.inv_tmpcount < 20 ):
                if (self.inv_rma_cbox.currentText() == "INVOICE"):
                    self.invqty = self.getinvoice_int()  
                    if (self.invqty > 0 ):
                        self.invmodel = self.confirm_data[1]
                        self.invname = self.confirm_data[2]
                        self.invsrp = self.confirm_data[4]                     
                        self.condb.toconfirm_db(self.iv,self.invmodel,self.invname,self.invsrp,self.invqty)
                    else:
                        QMessageBox.about(self, "About", "Please enter QTY", )
                elif (self.inv_rma_cbox.currentText() == "SRP"):
                    self.srpqty,self.srpsrp = self.getsrp_int()
                    if (self.srpqty > 0 ):
                        self.srpmodel = self.confirm_data[1]
                        self.srpname = self.confirm_data[2]
                        self.condb.toconfirm_db(self.iv,self.srpmodel,self.srpname,self.srpsrp,self.srpqty)
                    else:
                        QMessageBox.about(self, "About", "Please enter QTY", )
            else:
                QMessageBox.about(self, "About", "Over 20 items", )
            self.tot_am()
            self.ref()


    def toconfirm(self):
        self.tocf_list = []
        toconfirm_row = self.search_tv.currentIndex().row()
        for i in range(7):
            confirm = self.search_tv.model().data(self.search_tv.model().index(toconfirm_row, i))
            self.tocf_list.append(str(confirm))
        return self.tocf_list

    def getsrp_int(self):
        qty, ok = QInputDialog.getInt(self, "Please enter QTY", "Please enter QTY", 0, 1, 1000, 1)
        if ok:
            print(qty)
        srp, ok = QInputDialog.getInt(self, "Please enter SRP", "Please enter SRP", 0, 0, 2000000, 1)
        if ok:
            print(srp)
        return qty,srp
    def getinvoice_int(self):
        qty, ok = QInputDialog.getInt(self, "Please enter QTY", "Please enter QTY", 0, 1, 1000, 1)
        if ok:
            print(qty)
        return qty


    def delcon_data(self):
        self.contentslist = []
        curosor_row = self.confirm_tv.currentIndex().row()
        contents = self.confirm_tv.model().data(self.confirm_tv.model().index(curosor_row, 0))
        self.contentslist.append(str(contents))
        print(self.contentslist)
        id = self.contentslist[0]
        self.condb.del_conf_db(id)
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
        self.cm3_lineedit.clear()
        self.total_ed.clear()
        self.sales_lineedit.clear()
        self.salestel_lineedit.clear()
        self.cm1_lineedit.clear()
        self.cm2_lineedit.clear()

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
        self.inv_l_Model.setTable("invoice")
        self.inv_l_Model.setHeaderData(1, Qt.Horizontal, "Invoice No")
        self.inv_l_Model.select()
        while self.inv_l_Model.canFetchMore():
            self.inv_l_Model.fetchMore()

    def get_inv_cursor(self):
        self.inv_contentslist = []
        self.inv_curosor_row = self.inv_list_view.currentIndex().row()
        for i in range(96):
            contents = self.inv_list_view.model().data(self.inv_list_view.model().index(self.inv_curosor_row, i))
            self.inv_contentslist.append(str(contents))
        return self.inv_contentslist

    def inv_l_search_filter(self):
        self.inv_l_pFilterModel = QSortFilterProxyModel()
        self.inv_sear_ed.setPlaceholderText("Search here")
        self.inv_l_pFilterModel.setSourceModel(self.inv_l_Model)
        self.inv_l_pFilterModel.setFilterKeyColumn(1)
        self.inv_l_pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.inv_sear_ed.textChanged.connect(self.inv_l_pFilterModel.setFilterRegExp)

    def tot_am(self):
        total = self.condb.tot_am()
        print(total)
        self.total_ed.setText(str(total))


    def check_no(self):
        inva = self.inv_lineedit.text()
        inv = inva.upper()
        self.inv_lineedit.setText(inv)
        self.checkinfo = self.condb.check_invnum(inv)
        print(self.checkinfo)
        print(inv in self.checkinfo)
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
        self.call_invstat = callinv_list(self.info)
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
        self.confirm_tvModel.select()
        while self.confirm_tvModel.canFetchMore():
            self.confirm_tvModel.fetchMore()
        self.inv_l_Model.select()
        while self.inv_l_Model.canFetchMore():
            self.inv_l_Model.fetchMore()

    def client_listshow(self, val):
        contentslist = val
        self.billtolineedit.setText(contentslist[1])
        self.address_lineedit.setText(contentslist[2])
        self.attn_lineedit.setText(contentslist[3])
        self.tel__lineedit.setText(contentslist[4])
        self.cusid_lineedit.setText(contentslist[5])

    def clear_all(self):
        self.clear_invdata()
        self.condb.del_table()
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
    win = Callinvoice()
    win.show()
    sys.exit(app.exec_())
