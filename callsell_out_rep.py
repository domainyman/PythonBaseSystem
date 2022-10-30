# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QInputDialog, QHeaderView, QTableWidgetItem, \
    QLineEdit
import datetime
from sell_out_repui import Ui_sell_out_rep
from connectdb import database


class Callsell_out_rep(QMainWindow, Ui_sell_out_rep):
    def __init__(self, parent=None):
        super(Callsell_out_rep, self).__init__(parent)
        self.setupUi(self)
        self.da = datetime.date.today()
        self.le1 = QLineEdit()
        self.le2 = QLineEdit()
        self.condb = database()
        self.end_ed.setDate(QDate.currentDate())
        self.start_ed.setDate(QDate.currentDate())
        self.viewset()
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
        if (len(self.inv_noed.text()) != 0):
            da_st = self.start_ed.text()
            da_du = self.end_ed.text()
            inv_ed = self.inv_noed.text()
            self.sell_out_results = self.condb.sell_out_search(da_st, da_du,inv_ed)
            print(self.sell_out_results)
            self.tableWidget.setRowCount((len(self.sell_out_results) / 6))
            li = 0
            for i in range(int(len(self.sell_out_results) / 6)):
                for x in range(6):
                    self.tableWidget.setItem(i, x, QTableWidgetItem(self.sell_out_results[li]))
                    li = li + 1

    def listview(self):
        self.list_contentslist = []
        self.inv_curosor_row = self.tableWidget.currentIndex().row()
        for i in range(6):
            contents = self.tableWidget.model().data(self.tableWidget.model().index(self.inv_curosor_row, i))
            self.list_contentslist.append(contents)
        print(self.list_contentslist)
        self.data_info = self.condb.sell_outlistsearch(self.list_contentslist[0])
        print(self.data_info)
        self.in_li.setText(self.data_info[1])
        self.da_li.setText(self.data_info[2])
        self.billt_li.setText(self.data_info[3])
        self.addr_li.setText(self.data_info[4])
        self.attn_li.setText(self.data_info[5])
        self.tel_lu.setText(self.data_info[6])
        self.cusid_li.setText(self.data_info[7])
        self.dued_li.setText(self.data_info[8])
        self.sales_li.setText(self.data_info[9])
        self.saleste_li.setText(self.data_info[10])
        self.p1.setText(self.data_info[11])
        self.p1m.setText(self.data_info[12])
        self.p1c.setText(self.data_info[13])
        self.p1p.setText(self.data_info[14])
        self.p2.setText(self.data_info[15])
        self.p2m.setText(self.data_info[16])
        self.p2c.setText(self.data_info[17])
        self.p2p.setText(self.data_info[18])
        self.p3.setText(self.data_info[19])
        self.p3m.setText(self.data_info[20])
        self.p3c.setText(self.data_info[21])
        self.p3p.setText(self.data_info[22])
        self.p4.setText(self.data_info[23])
        self.p4m.setText(self.data_info[24])
        self.p4c.setText(self.data_info[25])
        self.p4p.setText(self.data_info[26])
        self.p5.setText(self.data_info[27])
        self.p5m.setText(self.data_info[28])
        self.p5c.setText(self.data_info[29])
        self.p5p.setText(self.data_info[30])
        self.p6.setText(self.data_info[31])
        self.p6m.setText(self.data_info[32])
        self.p6c.setText(self.data_info[33])
        self.p6p.setText(self.data_info[34])
        self.p7.setText(self.data_info[35])
        self.p7m.setText(self.data_info[36])
        self.p7c.setText(self.data_info[37])
        self.p7p.setText(self.data_info[38])
        self.p8.setText(self.data_info[39])
        self.p8m.setText(self.data_info[40])
        self.p8c.setText(self.data_info[41])
        self.p8p.setText(self.data_info[42])
        self.p9.setText(self.data_info[43])
        self.p9m.setText(self.data_info[44])
        self.p9c.setText(self.data_info[45])
        self.p9p.setText(self.data_info[46])
        self.p10.setText(self.data_info[47])
        self.p10m.setText(self.data_info[48])
        self.p10c.setText(self.data_info[49])
        self.p10p.setText(self.data_info[50])
        self.p11.setText(self.data_info[51])
        self.p11m.setText(self.data_info[52])
        self.p11c.setText(self.data_info[53])
        self.p11p.setText(self.data_info[54])
        self.p12.setText(self.data_info[55])
        self.p12m.setText(self.data_info[56])
        self.p12c.setText(self.data_info[57])
        self.p12p.setText(self.data_info[58])
        self.p13.setText(self.data_info[59])
        self.p13m.setText(self.data_info[60])
        self.p13c.setText(self.data_info[61])
        self.p13p.setText(self.data_info[62])
        self.p14.setText(self.data_info[63])
        self.p14m.setText(self.data_info[64])
        self.p14c.setText(self.data_info[65])
        self.p14p.setText(self.data_info[66])
        self.p15.setText(self.data_info[67])
        self.p15m.setText(self.data_info[68])
        self.p15c.setText(self.data_info[69])
        self.p15p.setText(self.data_info[70])
        self.p16.setText(self.data_info[71])
        self.p16m.setText(self.data_info[72])
        self.p16c.setText(self.data_info[73])
        self.p16p.setText(self.data_info[74])
        self.p17.setText(self.data_info[75])
        self.p17m.setText(self.data_info[76])
        self.p17c.setText(self.data_info[77])
        self.p17p.setText(self.data_info[78])
        self.p18.setText(self.data_info[79])
        self.p18m.setText(self.data_info[80])
        self.p18c.setText(self.data_info[81])
        self.p18p.setText(self.data_info[82])
        self.p19.setText(self.data_info[83])
        self.p19m.setText(self.data_info[84])
        self.p19c.setText(self.data_info[85])
        self.p19p.setText(self.data_info[86])
        self.p20.setText(self.data_info[87])
        self.p20m.setText(self.data_info[88])
        self.p20c.setText(self.data_info[89])
        self.p20p.setText(self.data_info[90])
        self.c1.setText(self.data_info[91])
        self.c2.setText(self.data_info[92])
        self.c3.setText(self.data_info[93])
        self.to_am_ed.setText(self.data_info[94])
        self.paym_ed.setText(self.data_info[95])

    def cheq_bu_click(self):
        self.inv_nosearch_bu.clicked.connect(self.search_data)
        self.tableWidget.clicked.connect(self.listview)

    def closeEvent(self, event):
        self.condb.closedb()
        print('window close')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Callsell_out_rep()
    win.show()
    sys.exit(app.exec_())