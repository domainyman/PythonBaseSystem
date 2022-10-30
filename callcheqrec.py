# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QInputDialog, QHeaderView, QTableWidgetItem, \
    QLineEdit
import datetime
from cheqrecui import Ui_cheqrec
from connectdb import database


class Callcheqrec(QMainWindow, Ui_cheqrec):
    def __init__(self, parent=None):
        super(Callcheqrec, self).__init__(parent)
        self.setupUi(self)
        self.da = datetime.date.today()
        self.le1 = QLineEdit()
        self.le2 = QLineEdit()
        self.condb = database()
        self.end_ed.setDate(QDate.currentDate())
        self.start_ed.setDate(QDate.currentDate())
        self.viewset()
        self.cn_viewset()
        self.cheq_bu_click()

    def viewset(self):
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setColumnWidth(0, 130)
        self.tableWidget.setColumnWidth(1, 130)
        self.tableWidget.setColumnWidth(2, 130)
        self.tableWidget.setColumnWidth(3, 130)
        self.tableWidget.setColumnWidth(4, 130)
        self.tableWidget.setHorizontalHeaderLabels(["Invoice No.", "Date.", "Shop", "Due Date", "Amount", "Payment"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.verticalHeader().setVisible(False)

    def search_data(self):
        da_st = self.start_ed.text()
        da_du = self.end_ed.text()
        self.cheq_results = self.condb.cheq_search(da_st, da_du)
        print(self.cheq_results)
        self.tableWidget.setRowCount((len(self.cheq_results) / 6))
        li = 0
        for i in range(int(len(self.cheq_results) / 6)):
            for x in range(6):
                self.tableWidget.setItem(i, x, QTableWidgetItem(self.cheq_results[li]))
                li = li + 1

    def paybox(self):
        items = ("No", "Yes")
        item, ok = QInputDialog.getItem(self, "Payment Status", "Status", items, 0, False)
        if ok and item:
            self.le1.setText(item)
            self.toconfirm()

    def toconfirm(self):
        toconfirm_row = self.tableWidget.currentIndex().row()
        tocf_list = []
        for i in range(6):
            confirm = self.tableWidget.model().data(self.tableWidget.model().index(toconfirm_row, i))
            tocf_list.append(str(confirm))
        inv_nu = tocf_list[0]
        namci = tocf_list[2]
        pay_st = self.le1.text()
        self.condb.chequplpaym_db(inv_nu, namci, pay_st)
        self.le1.clear()
        self.search_det()

    def inv_search(self):
        if (len(self.inv_noed.text())) != 0:
            inv_ed = self.inv_noed.text()
            self.cheqinv_results = self.condb.cheqinvsearch_db(inv_ed)
            print(self.cheqinv_results)
            self.tableWidget.setRowCount((len(self.cheqinv_results) / 6))
            li = 0
            for i in range(int(len(self.cheqinv_results) / 6)):
                for x in range(6):
                    self.tableWidget.setItem(i, x, QTableWidgetItem(self.cheqinv_results[li]))
                    li = li + 1
        else:
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)

    def search_det(self):
        if (len(self.inv_noed.text())) != 0:
            self.inv_search()
        elif str(self.start_ed.text()) == str(self.da):
            self.unpaid()
        else:
            self.search_data()

    def unpaid(self):
        self.chequnpaid_search = self.condb.chequnpaid_search()
        print(self.chequnpaid_search)
        print((len(self.chequnpaid_search)))
        print((len(self.chequnpaid_search) / 6))
        self.tableWidget.setRowCount((len(self.chequnpaid_search) / 6))
        li = 0
        for i in range(int(len(self.chequnpaid_search) / 6)):
            for x in range(6):
                self.tableWidget.setItem(i, x, QTableWidgetItem(self.chequnpaid_search[li]))
                li = li + 1

    # cn view
    def cn_viewset(self):
        self.cn_tabw.setColumnCount(5)
        self.cn_tabw.setColumnWidth(0, 130)
        self.cn_tabw.setColumnWidth(1, 130)
        self.cn_tabw.setColumnWidth(2, 130)
        self.cn_tabw.setColumnWidth(3, 130)
        self.cn_tabw.setHorizontalHeaderLabels(["CN No.", "Date.", "Shop", "Amount", "Payment"])
        self.cn_tabw.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.cn_tabw.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.cn_tabw.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.cn_tabw.setSortingEnabled(True)
        self.cn_tabw.verticalHeader().setVisible(False)

    def cn_search_data(self):
        da_st = self.start_ed.text()
        da_du = self.end_ed.text()
        self.cn_results = self.condb.cn_search(da_st, da_du)
        self.cn_tabw.setRowCount((len(self.cn_results) / 5))
        li = 0
        for i in range(int(len(self.cn_results) / 5)):
            for x in range(5):
                self.cn_tabw.setItem(i, x, QTableWidgetItem(self.cn_results[li]))
                li = li + 1

    def cn_paybox(self):
        items = ("No", "Yes")
        item, ok = QInputDialog.getItem(self, "Payment Status", "Status", items, 0, False)
        if ok and item:
            self.le2.setText(item)
            self.cn_toconfirm()

    def cn_toconfirm(self):
        toconfirm_row = self.cn_tabw.currentIndex().row()
        tocf_list = []
        for i in range(5):
            confirm = self.cn_tabw.model().data(self.cn_tabw.model().index(toconfirm_row, i))
            tocf_list.append(str(confirm))
        cn_nu = tocf_list[0]
        namci = tocf_list[2]
        pay_st = self.le2.text()
        self.condb.cn_uplpaym_db(cn_nu, namci, pay_st)
        self.condb.commitdb()
        self.le2.clear()
        self.cn_search_det()

    def cn_search(self):
        if (len(self.cn_noed.text())) != 0:
            cn_ed = self.cn_noed.text()
            self.cninv_results = self.condb.cninvsearch_db(cn_ed)
            self.cn_tabw.setRowCount((len(self.cninv_results) / 5))
            li = 0
            for i in range(int(len(self.cninv_results) / 5)):
                for x in range(5):
                    self.cn_tabw.setItem(i, x, QTableWidgetItem(self.cninv_results[li]))
                    li = li + 1
        else:
            self.cn_tabw.clearContents()
            self.cn_tabw.setRowCount(0)

    def cn_search_det(self):
        if (len(self.cn_noed.text())) != 0:
            self.cn_search()
        elif str(self.start_ed.text()) == str(self.da):
            self.cn_unpaid()
        else:
            self.cn_search_data()

    def cn_unpaid(self):
        self.cnunpaid_search = self.condb.cn_unpaid_search()
        print(self.cnunpaid_search)
        print((len(self.cnunpaid_search)))
        print((len(self.cnunpaid_search) / 5))
        self.cn_tabw.setRowCount((len(self.cnunpaid_search) / 5))
        self.cn_li = 0
        for i in range(int(len(self.cnunpaid_search) / 5)):
            for x in range(5):
                self.cn_tabw.setItem(i, x, QTableWidgetItem(self.cnunpaid_search[self.cn_li]))
                self.cn_li = self.cn_li + 1

    def cheq_bu_click(self):
        self.Search_bu.clicked.connect(self.search_data)
        self.Search_bu.clicked.connect(self.cn_search_data)
        self.tableWidget.clicked.connect(self.paybox)
        self.inv_nosearch_bu.clicked.connect(self.inv_search)
        self.unpaid_bu.clicked.connect(self.unpaid)
        self.cn_tabw.clicked.connect(self.cn_paybox)
        self.cn_nosearch_bu.clicked.connect(self.cn_search)
        self.cn_unpaid_bu.clicked.connect(self.cn_unpaid)

    def closeEvent(self, event):
        self.condb.closedb()
        print('window close')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Callcheqrec()
    win.show()
    sys.exit(app.exec_())
