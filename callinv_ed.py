# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QInputDialog, QMessageBox, QHeaderView, \
    QTableWidgetItem
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QDate
import datetime
from in_edui import Ui_in_ed
from connectdb import database


class Callin_ed(QMainWindow, Ui_in_ed):
    def __init__(self, parent=None):
        super(Callin_ed, self).__init__(parent)
        self.setupUi(self)
        self.da = datetime.date.today()
        self.condb = database()   
        self.inv_l_setupModel()
        self.inv_l_search_filter()
        self.inv_l_setupView()
        self.search_tv_setupModel()
        self.search_tv_search_filter()
        self.search_tv_setupView()
        self.confirm_tv_setupModel()
        self.confirm_tv_setupView()
        self.cheq_bu_click()
        self.clear_showtable()

    def show_inv(self,inv_info):
        self.in_li.setText(inv_info[1])
        self.da_li.setText(inv_info[2])
        self.billt_li.setText(inv_info[3])
        self.addr_li.setText(inv_info[4])
        self.attn_li.setText(inv_info[5])
        self.tel_lu.setText(inv_info[6])
        self.cusid_li.setText(inv_info[7])
        self.dued_li.setText(inv_info[8])
        self.sales_li.setText(inv_info[9])
        self.saleste_li.setText(inv_info[10])
        self.p1.setText(inv_info[11])
        self.p1m.setText(inv_info[12])
        self.p1c.setText(inv_info[13])
        self.p1p.setText(inv_info[14])
        self.p2.setText(inv_info[15])
        self.p2m.setText(inv_info[16])
        self.p2c.setText(inv_info[17])
        self.p2p.setText(inv_info[18])
        self.p3.setText(inv_info[19])
        self.p3m.setText(inv_info[20])
        self.p3c.setText(inv_info[21])
        self.p3p.setText(inv_info[22])
        self.p4.setText(inv_info[23])
        self.p4m.setText(inv_info[24])
        self.p4c.setText(inv_info[25])
        self.p4p.setText(inv_info[26])
        self.p5.setText(inv_info[27])
        self.p5m.setText(inv_info[28])
        self.p5c.setText(inv_info[29])
        self.p5p.setText(inv_info[30])
        self.p6.setText(inv_info[31])
        self.p6m.setText(inv_info[32])
        self.p6c.setText(inv_info[33])
        self.p6p.setText(inv_info[34])
        self.p7.setText(inv_info[35])
        self.p7m.setText(inv_info[36])
        self.p7c.setText(inv_info[37])
        self.p7p.setText(inv_info[38])
        self.p8.setText(inv_info[39])
        self.p8m.setText(inv_info[40])
        self.p8c.setText(inv_info[41])
        self.p8p.setText(inv_info[42])
        self.p9.setText(inv_info[43])
        self.p9m.setText(inv_info[44])
        self.p9c.setText(inv_info[45])
        self.p9p.setText(inv_info[46])
        self.p10.setText(inv_info[47])
        self.p10m.setText(inv_info[48])
        self.p10c.setText(inv_info[49])
        self.p10p.setText(inv_info[50])
        self.p11.setText(inv_info[51])
        self.p11m.setText(inv_info[52])
        self.p11c.setText(inv_info[53])
        self.p11p.setText(inv_info[54])
        self.p12.setText(inv_info[55])
        self.p12m.setText(inv_info[56])
        self.p12c.setText(inv_info[57])
        self.p12p.setText(inv_info[58])
        self.p13.setText(inv_info[59])
        self.p13m.setText(inv_info[60])
        self.p13c.setText(inv_info[61])
        self.p13p.setText(inv_info[62])
        self.p14.setText(inv_info[63])
        self.p14m.setText(inv_info[64])
        self.p14c.setText(inv_info[65])
        self.p14p.setText(inv_info[66])
        self.p15.setText(inv_info[67])
        self.p15m.setText(inv_info[68])
        self.p15c.setText(inv_info[69])
        self.p15p.setText(inv_info[70])
        self.p16.setText(inv_info[71])
        self.p16m.setText(inv_info[72])
        self.p16c.setText(inv_info[73])
        self.p16p.setText(inv_info[74])
        self.p17.setText(inv_info[75])
        self.p17m.setText(inv_info[76])
        self.p17c.setText(inv_info[77])
        self.p17p.setText(inv_info[78])
        self.p18.setText(inv_info[79])
        self.p18m.setText(inv_info[80])
        self.p18c.setText(inv_info[81])
        self.p18p.setText(inv_info[82])
        self.p19.setText(inv_info[83])
        self.p19m.setText(inv_info[84])
        self.p19c.setText(inv_info[85])
        self.p19p.setText(inv_info[86])
        self.p20.setText(inv_info[87])
        self.p20m.setText(inv_info[88])
        self.p20c.setText(inv_info[89])
        self.p20p.setText(inv_info[90])
        self.c1.setText(inv_info[91])
        self.c2.setText(inv_info[92])
        self.c3.setText(inv_info[93])
        self.to_am_ed.setText(inv_info[94])
        self.paym_ed.setText(inv_info[95])

    def clear_list(self):
        self.in_li.clear()
        self.da_li.clear()
        self.billt_li.clear()
        self.addr_li.clear()
        self.attn_li.clear()
        self.tel_lu.clear()
        self.cusid_li.clear()
        self.dued_li.clear()
        self.sales_li.clear()
        self.saleste_li.clear()
        self.p1.clear()
        self.p1m.clear()
        self.p1c.clear()
        self.p1p.clear()
        self.p2.clear()
        self.p2m.clear()
        self.p2c.clear()
        self.p2p.clear()
        self.p3.clear()
        self.p3m.clear()
        self.p3c.clear()
        self.p3p.clear()
        self.p4.clear()
        self.p4m.clear()
        self.p4c.clear()
        self.p4p.clear()
        self.p5.clear()
        self.p5m.clear()
        self.p5c.clear()
        self.p5p.clear()
        self.p6.clear()
        self.p6m.clear()
        self.p6c.clear()
        self.p6p.clear()
        self.p7.clear()
        self.p7m.clear()
        self.p7c.clear()
        self.p7p.clear()
        self.p8.clear()
        self.p8m.clear()
        self.p8c.clear()
        self.p8p.clear()
        self.p9.clear()
        self.p9m.clear()
        self.p9c.clear()
        self.p9p.clear()
        self.p10.clear()
        self.p10m.clear()
        self.p10c.clear()
        self.p10p.clear()
        self.p11.clear()
        self.p11m.clear()
        self.p11c.clear()
        self.p11p.clear()
        self.p12.clear()
        self.p12m.clear()
        self.p12c.clear()
        self.p12p.clear()
        self.p13.clear()
        self.p13m.clear()
        self.p13c.clear()
        self.p13p.clear()
        self.p14.clear()
        self.p14m.clear()
        self.p14c.clear()
        self.p14p.clear()
        self.p15.clear()
        self.p15m.clear()
        self.p15c.clear()
        self.p15p.clear()
        self.p16.clear()
        self.p16m.clear()
        self.p16c.clear()
        self.p16p.clear()
        self.p17.clear()
        self.p17m.clear()
        self.p17c.clear()
        self.p17p.clear()
        self.p18.clear()
        self.p18m.clear()
        self.p18c.clear()
        self.p18p.clear()
        self.p19.clear()
        self.p19m.clear()
        self.p19c.clear()
        self.p19p.clear()
        self.p20.clear()
        self.p20m.clear()
        self.p20c.clear()
        self.p20p.clear()
        self.c1.clear()
        self.c2.clear()
        self.c3.clear()
        self.to_am_ed.clear()
        self.paym_ed.clear()

    def confirm_tv_setupView(self):
        self.in_item_new_tv.setModel(self.confirm_tvModel)
        self.in_item_new_tv.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.in_item_new_tv.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.in_item_new_tv.setColumnWidth(0, 40)
        self.in_item_new_tv.setColumnWidth(1, 80)
        self.in_item_new_tv.setColumnWidth(2, 100)
        self.in_item_new_tv.setColumnWidth(3, 200)
        self.in_item_new_tv.setColumnWidth(4, 80)
        self.in_item_new_tv.setColumnWidth(5, 80)

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


    def inv_l_setupView(self):
        self.inv_list_tv.setModel(self.inv_l_pFilterModel)
        self.inv_list_tv.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.inv_list_tv.verticalHeader().hide()
        self.inv_list_tv.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.inv_list_tv.setSortingEnabled(True)
        self.inv_list_tv.setColumnWidth(1, 170)
        self.inv_list_tv.setColumnHidden(0, True)
        for x in range(2, 96):
            self.inv_list_tv.setColumnHidden(x, True)

    def inv_l_setupModel(self):
        self.inv_l_Model = QSqlTableModel()
        self.inv_l_Model.setTable("invoice")
        self.inv_l_Model.setHeaderData(1, Qt.Horizontal, "Invoice No")
        self.inv_l_Model.select()
        while self.inv_l_Model.canFetchMore():
            self.inv_l_Model.fetchMore()

    def inv_l_search_filter(self):
        self.inv_l_pFilterModel = QSortFilterProxyModel()
        self.search_ed.setPlaceholderText("Search here")
        self.inv_l_pFilterModel.setSourceModel(self.inv_l_Model)
        self.inv_l_pFilterModel.setFilterKeyColumn(1)
        self.inv_l_pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.search_ed.textChanged.connect(self.inv_l_pFilterModel.setFilterRegExp)


    def search_tv_setupView(self):
        self.prod_list_tv.setModel(self.search_tv_pFilterModel)
        self.prod_list_tv.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.prod_list_tv.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.prod_list_tv.setColumnWidth(0, 40)
        self.prod_list_tv.setColumnWidth(2, 200)
        self.prod_list_tv.setColumnWidth(4, 50)
        self.prod_list_tv.setColumnWidth(5, 50)
        self.prod_list_tv.setColumnWidth(6, 50)

    def search_tv_setupModel(self):
        self.prod_list_tv_Model = QSqlTableModel()
        self.prod_list_tv_Model.setTable("lib")
        self.search_tv__getFieldNames()
        self.prod_list_tv_Model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.prod_list_tv_Model.setHeaderData(self.fldNum["id"], Qt.Horizontal, "ID")
        self.prod_list_tv_Model.setHeaderData(self.fldNum["model"], Qt.Horizontal, "Model")
        self.prod_list_tv_Model.setHeaderData(self.fldNum["name"], Qt.Horizontal, "Name")
        self.prod_list_tv_Model.setHeaderData(self.fldNum["cost"], Qt.Horizontal, "Cost")
        self.prod_list_tv_Model.setHeaderData(self.fldNum["srp"], Qt.Horizontal, "SRP")
        self.prod_list_tv_Model.setHeaderData(self.fldNum["stock"], Qt.Horizontal, "Stock")
        self.prod_list_tv_Model.setHeaderData(self.fldNum["rma"], Qt.Horizontal, "RMA")
        self.prod_list_tv_Model.select()
        while self.prod_list_tv_Model.canFetchMore():
            self.prod_list_tv_Model.fetchMore()

    def search_tv_search_filter(self):
        self.search_tv_pFilterModel = QSortFilterProxyModel()
        self.prod_serach_ed.setPlaceholderText("Search here")
        self.search_tv_pFilterModel.setSourceModel(self.prod_list_tv_Model)
        self.search_tv_pFilterModel.setFilterKeyColumn(-1)
        self.search_tv_pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.prod_serach_ed.textChanged.connect(self.search_tv_pFilterModel.setFilterRegExp)

    def search_tv__getFieldNames(self):
        self.emptyRec = self.prod_list_tv_Model.record()
        self.fldNum = {}
        for i in range(self.emptyRec.count()):
            fieldName = self.emptyRec.fieldName(i)
            self.fldNum.setdefault(fieldName)
            self.fldNum[fieldName] = i

    def get_inv_cursor(self):
        self.inv_itemslist = []
        self.inv_curosor_row = self.inv_list_tv.currentIndex().row()
        for i in range(96):
            contents = self.inv_list_tv.model().data(self.inv_list_tv.model().index(self.inv_curosor_row, i))
            self.inv_itemslist.append(str(contents))
        return self.inv_itemslist

    def activeinv(self):
        self.condb.del_table()
        self.info = self.get_inv_cursor()
        self.show_inv(self.info)
        self.re_select()


    def changeinv(self):
        if (len(self.in_li.text()) != 0 ):
            reply = QMessageBox.information(self, "Edit INVOICE", "Once Edit , Invoice cannot be recovered!",QMessageBox.Yes | QMessageBox.Close, QMessageBox.Close)
            if reply == QMessageBox.Yes :
                self.upload_bu.setEnabled(True)
                self.upload_edit.setEnabled(False)
                self.inv_list_tv.setEnabled(False)
                self.in_item_new_tv.setEnabled(True)
                self.prod_list_tv.setEnabled(True)
                self.iv = self.in_li.text()
                self.invdata = self.condb.select_inv(self.iv)
                print(self.invdata)
                self.firdata = self.invdata[11:91]
                print(self.firdata)
                self.reindata = [i for i in self.firdata if i != '']
                print(self.reindata)
                self.exc_res = self.condb.excision_results(self.reindata,4)
                print(self.exc_res)
                self.restoconfirm(self.exc_res,self.iv)


    def restoconfirm(self,info,iv):
        for step in range(len(info)):
            self.itemmodel = info[step][0]
            self.itemname = info[step][1]
            self.itemqty = info[step][2]
            self.itemprice = info[step][3]
            self.condb.toconfirm_db(iv,self.itemmodel,self.itemname,self.itemprice,self.itemqty)
            self.confirm_tvModel.select()
            while self.confirm_tvModel.canFetchMore():
                self.confirm_tvModel.fetchMore()


    def delcon_data(self):
        self.contentslist = []
        curosor_row = self.in_item_new_tv.currentIndex().row()    
        contents = self.in_item_new_tv.model().data(self.in_item_new_tv.model().index(curosor_row, 0))
        self.contentslist.append(str(contents))
        print(self.contentslist)
        id = self.contentslist[0]
        self.condb.del_conf_db(id)
        self.tot_am()
        self.confirm_tvModel.submitAll()
        self.confirm_tvModel.select()
        while self.confirm_tvModel.canFetchMore():
            self.confirm_tvModel.fetchMore()

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



    def toconfirm(self):
        self.tocf_list = []
        toconfirm_row = self.prod_list_tv.currentIndex().row()
        for i in range(7):
            confirm = self.prod_list_tv.model().data(self.prod_list_tv.model().index(toconfirm_row, i))
            self.tocf_list.append(str(confirm))
        return self.tocf_list

    def getcomf_int(self):
        if (len(self.in_li.text()) != 0):
            self.iv = self.in_li.text()
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
            self.re_select()
              

    def renewinv(self):
        self.count = self.condb.inv_tmpco()
        if (self.count != 0):
            reply = QMessageBox.information(self, "Renew INVOICE", "Once Renew , Invoice cannot be recovered!",
                                            QMessageBox.Yes | QMessageBox.Close, QMessageBox.Close)
            if reply == QMessageBox.Yes and (len(self.in_li.text()) != 0) :
                self.iv = self.in_li.text()
                self.invdata = self.condb.select_inv(self.iv)
                self.firdata = self.invdata[11:91]
                self.reindata = [i for i in self.firdata if i != '']
                self.exc_res = self.condb.excision_results(self.reindata,4)
                print(self.exc_res)
                self.condb.delinv_stock(self.exc_res)
                self.clear_invitem = self.clearexc_res(self.exc_res)
                print(self.clear_invitem)
                self.cap = self.condb.capselect_db()
                self.addexc_res = self.condb.excision_results(self.cap,5)
                self.stock_iv,self.res = self.condb.upload_all_prod_inv(self.addexc_res)
                self.condb.upl_prodqty(self.res)
                self.setam = self.to_am_ed.text()
                self.condb.upload_toam(self.iv,self.setam)
                self.clear_showtable()

            else:
                QMessageBox.about(self, "About", "Please Enter Info Correctly!", )
        else:
            QMessageBox.about(self, "About", "Please Enter Info Correctly!", )
    
    def clearexc_res(self,data):
        for step in range(len(data)):
            for substep in range(len(data[step])):
                data[step][substep] = ""
        return data

    def tot_am(self):
        total = self.condb.tot_am()
        print(total)
        self.to_am_ed.setText(str(total))

    def cheq_bu_click(self):
        self.inv_list_tv.clicked.connect(self.activeinv)
        self.in_item_new_tv.clicked.connect(self.delcon_data)
        self.prod_list_tv.clicked.connect(self.getcomf_int)
        self.upload_bu.clicked.connect(self.renewinv)
        self.upload_edit.clicked.connect(self.changeinv)
        self.clear_bu.clicked.connect(self.clear_showtable)

    def closeEvent(self, event):
        self.clear_showtable()
        self.condb.closedb()
        print('window close')

    def re_select(self):
        self.confirm_tvModel.select()
        while self.confirm_tvModel.canFetchMore():
            self.confirm_tvModel.fetchMore()
        self.prod_list_tv_Model.select()
        while self.prod_list_tv_Model.canFetchMore():
            self.prod_list_tv_Model.fetchMore()
        self.inv_l_Model.select()
        while self.inv_l_Model.canFetchMore():
            self.inv_l_Model.fetchMore()

    def clear_showtable(self):
        self.condb.del_table()
        self.clear_list()
        self.upload_bu.setEnabled(False)
        self.upload_edit.setEnabled(True)
        self.inv_list_tv.setEnabled(True)
        self.in_item_new_tv.setEnabled(False)
        self.prod_list_tv.setEnabled(False)
        self.re_select()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Callin_ed()
    win.show()
    sys.exit(app.exec_())
