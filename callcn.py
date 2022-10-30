# -*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import Qt, QSortFilterProxyModel, QDate
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QMessageBox
from callclient_list import Callclient_list
from callcn_list import callinv_list
from callcompinfo import Callcompinfo
from cnui import Ui_cn
from connectdb import database


class Callcn(QMainWindow, Ui_cn):
    def __init__(self, parent=None):
        super(Callcn, self).__init__(parent)
        dbl_validator = QDoubleValidator(self)
        dbl_validator.setNotation(QDoubleValidator.StandardNotation)
        dbl_validator.setDecimals(6)
        int_validator = QIntValidator(self)
        int_validator.setRange(0, 9999999)
        self.setupUi(self)
        self.pri_ed.setValidator(dbl_validator)
        self.qty_ed.setValidator(int_validator)
        self.date_lineedit.setDate(QDate.currentDate())
        self.dued_lineedit.setDate(QDate.currentDate())
        self.condb = database()
        self.cn_bu_click()
        self.cnview_setupModel()
        self.cnview_setupView()
        self.cn_l_setupModel()
        self.cn_l_search_filter()
        self.cn_l_setupView()
        self.clear_all()

    def cnview_setupView(self):
        self.conf_treeView.setModel(self.cnview_Model)
        self.conf_treeView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.conf_treeView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.conf_treeView.setColumnWidth(0, 40)
        self.conf_treeView.setColumnWidth(2, 150)
        self.conf_treeView.setColumnWidth(3, 250)
        self.conf_treeView.setColumnWidth(4, 100)
        self.conf_treeView.setColumnWidth(5, 100)

    def cnview_setupModel(self):
        self.cnview_Model = QSqlTableModel()
        self.cnview_Model.setTable("cn_tmp")
        self.cnview_getFieldNames()
        self.cnview_Model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.cnview_Model.setHeaderData(self.fldNum["id"], Qt.Horizontal, "ID")
        self.cnview_Model.setHeaderData(self.fldNum["iv"], Qt.Horizontal, "NO.")
        self.cnview_Model.setHeaderData(self.fldNum["p1m"], Qt.Horizontal, "Item Model")
        self.cnview_Model.setHeaderData(self.fldNum["p1"], Qt.Horizontal, "Item Name")
        self.cnview_Model.setHeaderData(self.fldNum["p1c"], Qt.Horizontal, "Price")
        self.cnview_Model.setHeaderData(self.fldNum["p1p"], Qt.Horizontal, "Qty")
        self.cnview_Model.select()
        while self.cnview_Model.canFetchMore():
            self.cnview_Model.fetchMore()

    def cnview_getFieldNames(self):
        self.emptyRec = self.cnview_Model.record()
        self.fldNum = {}
        for i in range(self.emptyRec.count()):
            fieldName = self.emptyRec.fieldName(i)
            self.fldNum.setdefault(fieldName)
            self.fldNum[fieldName] = i

    def upladdcn_data(self):
        if (len(self.cn_lineedit.text())) != 0 and (len(self.it_ed.text())) != 0 and (len(self.de_ed.text())) != 0 \
                and (len(self.pri_ed.text())) != 0 and (len(self.qty_ed.text())) != 0:
            inv = self.cn_lineedit.text()
            model = self.it_ed.text()
            des = self.de_ed.text()
            price = self.pri_ed.text()
            qty = self.qty_ed.text()
            self.cn_tmpcount = self.condb.cn_tmpco()
            if self.cn_tmpcount < 10:
                self.condb.upl_cn_db(inv, model, des, price, qty)
                self.totcn_am()
                self.clear_addcn_data()
            else:
                QMessageBox.about(self, "About", "Over 10 items", )
            self.cnview_Model.submitAll()
            self.cnview_Model.select()
            while self.cnview_Model.canFetchMore():
                self.cnview_Model.fetchMore()
        else:
            QMessageBox.about(self, "About", "Repeat! Please Check Data. !", )

    def delcn_data(self):
        curosor_row = self.conf_treeView.currentIndex().row()
        contentslist = []
        contents = self.conf_treeView.model().data(self.conf_treeView.model().index(curosor_row, 3))
        contentslist.append(str(contents))
        print(contentslist)
        na = contentslist[0]
        self.condb.del_cntmp_db(na)
        self.totcn_am()
        self.cnview_Model.submitAll()
        self.cnview_Model.select()
        while self.cnview_Model.canFetchMore():
            self.cnview_Model.fetchMore()

    def clear_addcn_data(self):
        self.it_ed.clear()
        self.de_ed.clear()
        self.pri_ed.clear()
        self.qty_ed.clear()

    def cn_add_data(self):
        if ((len(self.cn_lineedit.text())) != 0 and (len(self.billtolineedit.text())) != 0 and (
                len(self.address_lineedit.text())) != 0
                and (len(self.cusid_lineedit.text())) != 0 and (self.cnview_Model.rowCount() > 0)):
            reply = QMessageBox.information(self, "Add CN", "Add CN ? ",
                                            QMessageBox.Yes | QMessageBox.Close, QMessageBox.Close)
            if reply == QMessageBox.Yes:
                iv = self.cn_lineedit.text()
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
                amount = self.am_ed.text()
                self.checkinfo = self.condb.check_cnnum(iv)
                print(iv in self.checkinfo)
                if (iv in self.checkinfo) is False:
                    self.condb.cn_add_db_p1(iv, da, bi, ad, at, te, ci, du, sa, sl, c1, c2, c3, amount)
                    self.cap = self.condb.cn_capselect_db()
                    self.exc_res = self.condb.excision_results(self.cap,5)
                    self.condb.upload_all_prod_cn(self.exc_res)

                else:
                    QMessageBox.about(self, "About", "Repeat! Please Check NO./PI. !", )
                    self.condb.del_cn_table()
                    self.cnview_Model.select()
                    while self.cnview_Model.canFetchMore():
                        self.cnview_Model.fetchMore()
                self.clear_all()
        else:
            QMessageBox.about(self, "About", "Please Enter Info Correctly!", )

    def checkBoxChangedAction(self, state):
        if state == Qt.Checked:
            self.checkinfo = self.condb.check_cnnum(self.cn_lineedit.text())
            if (self.cn_lineedit.text() in self.checkinfo) is True:
                QMessageBox.about(self, "About", "Repeat! Please Check NO./PI. !", )
                self.cn_lineedit.setEnabled(True)
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
                self.conf_treeView.setEnabled(False)
                self.it_ed.setEnabled(False)
                self.de_ed.setEnabled(False)
                self.pri_ed.setEnabled(False)
                self.qty_ed.setEnabled(False)
            elif (self.cn_lineedit.text() in self.checkinfo) is False:
                self.cn_lineedit.setEnabled(False)
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
                if (len(self.cn_lineedit.text())) != 0:
                    self.conf_treeView.setEnabled(True)
                    self.it_ed.setEnabled(True)
                    self.de_ed.setEnabled(True)
                    self.pri_ed.setEnabled(True)
                    self.qty_ed.setEnabled(True)
                else:
                    self.conf_treeView.setEnabled(False)
                    self.it_ed.setEnabled(False)
                    self.de_ed.setEnabled(False)
                    self.pri_ed.setEnabled(False)
                    self.qty_ed.setEnabled(False)
        else:
            self.cn_lineedit.setEnabled(True)
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
            self.conf_treeView.setEnabled(False)
            self.it_ed.setEnabled(False)
            self.de_ed.setEnabled(False)
            self.pri_ed.setEnabled(False)
            self.qty_ed.setEnabled(False)

    def clear_cndata(self):
        self.cn_lineedit.clear()
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
        self.am_ed.clear()

    def cn_l_setupView(self):
        self.cn_list_view.setModel(self.cn_l_pFilterModel)
        self.cn_list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.cn_list_view.verticalHeader().hide()
        self.cn_list_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.cn_list_view.setSortingEnabled(True)
        self.cn_list_view.setColumnWidth(1, 210)
        self.cn_list_view.setColumnHidden(0, True)
        for x in range(2, 56):
            self.cn_list_view.setColumnHidden(x, True)

    def cn_l_setupModel(self):
        self.cn_l_Model = QSqlTableModel()
        self.cn_l_Model.setTable("cn")
        self.cn_l_Model.setHeaderData(1, Qt.Horizontal, "CN No")
        self.cn_l_Model.select()
        while self.cn_l_Model.canFetchMore():
            self.cn_l_Model.fetchMore()

    def cn_l_search_filter(self):
        self.cn_l_pFilterModel = QSortFilterProxyModel()
        self.cn_sear_ed.setPlaceholderText("Search here")
        self.cn_l_pFilterModel.setSourceModel(self.cn_l_Model)
        self.cn_l_pFilterModel.setFilterKeyColumn(1)
        self.cn_l_pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.cn_sear_ed.textChanged.connect(self.cn_l_pFilterModel.setFilterRegExp)

    def get_cn_cursor(self):
        self.cn_contentslist = []
        self.cn_curosor_row = self.cn_list_view.currentIndex().row()
        for i in range(56):
            contents = self.cn_list_view.model().data(self.cn_list_view.model().index(self.cn_curosor_row, i))
            self.cn_contentslist.append(str(contents))
        return self.cn_contentslist


    def c_cnstat(self):
        self.info = self.get_cn_cursor()
        self.call_cnstat = callinv_list(self.info)
        self.call_cnstat.my_Signal.connect(self.clear_all)
        self.call_cnstat.show()

    def totcn_am(self):
        total = self.condb.tot_cn_am()
        print(total)
        self.am_ed.setText(str(total))

    def c_client_list(self):
        self.call_client_list = Callclient_list()
        self.call_client_list.my_Signal.connect(self.client_listshow)
        self.call_client_list.show()

    def client_listshow(self, val):
        contentslist = val
        self.billtolineedit.setText(contentslist[1])
        self.address_lineedit.setText(contentslist[2])
        self.attn_lineedit.setText(contentslist[3])
        self.tel__lineedit.setText(contentslist[4])
        self.cusid_lineedit.setText(contentslist[5])

    def check_no(self):
        inva = self.cn_lineedit.text()
        inv = inva.upper()
        self.cn_lineedit.setText(inv)
        self.checkinfo = self.condb.check_cnnum(inv)
        print(inv in self.checkinfo)
        if (inv in self.checkinfo) is True:
            QMessageBox.about(self, "About", "Repeat! Please Check NO./PI. !", )
            self.cn_lineedit.clear()

        if (inv in self.checkinfo) is False:
            pass

    def cn_bu_click(self):
        self.enter.clicked.connect(self.cn_add_data)
        self.Lock_cb.stateChanged.connect(self.checkBoxChangedAction)
        self.clear.clicked.connect(self.clear_all)
        self.companyinfo.clicked.connect(self.c_compinfo)
        self.pushButton.clicked.connect(self.upladdcn_data)
        self.conf_treeView.clicked.connect(self.delcn_data)
        self.cn_list_view.clicked.connect(self.c_cnstat)
        self.client.clicked.connect(self.c_client_list)
        self.cn_lineedit.editingFinished.connect(self.check_no)

    def c_compinfo(self):
        self.call_cominfo = Callcompinfo()
        self.call_cominfo.show()

    def clear_all(self):
        self.clear_cndata()
        self.condb.del_cn_table()
        self.conf_treeView.setEnabled(False)
        self.Lock_cb.setChecked(False)
        self.it_ed.setEnabled(False)
        self.de_ed.setEnabled(False)
        self.pri_ed.setEnabled(False)
        self.qty_ed.setEnabled(False)
        self.cnview_Model.select()
        while self.cnview_Model.canFetchMore():
            self.cnview_Model.fetchMore()
        self.cn_l_Model.select()
        while self.cn_l_Model.canFetchMore():
            self.cn_l_Model.fetchMore()

    def closeEvent(self, event):
        self.clear_all()
        self.condb.closedb()
        print('window close')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Callcn()
    win.show()
    sys.exit(app.exec_())
