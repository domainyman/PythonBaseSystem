# -*- coding: utf-8 -*-
import decimal
import sys
import random
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QApplication, QMessageBox


class database(object):

    def __init__(self):
        self.DB_LOCATION = "viewmaxdb.db"
        decimal.getcontext().rounding = "ROUND_HALF_UP"
        if QSqlDatabase.contains("qt_sql_default_connection"):
            self.conn = QSqlDatabase.database("qt_sql_default_connection")
            print("qt_sql_default_connection")
            self.check_db()
        else:
            self.conn = QSqlDatabase.addDatabase("QSQLITE")
            print("SQLITE")
            self.conn.setDatabaseName(self.DB_LOCATION)
            self.check_db()

    def check_db(self):
        self.checkdb = None
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.exec_("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='lib'")
            while query.next():
                self.checkdb = query.value(0)
            print(self.checkdb)
            if self.checkdb == 0:
                self.createtable()
                print('Create_table Done')
            else:
                print('NOT Need Create_table')

    def createtable(self):
        if not self.conn.open():
            print("Cannot open Database")
        else:
            query = QSqlQuery(self.conn)
            query.exec_(
                "CREATE TABLE lib ("
                "id INTEGER primary key AUTOINCREMENT,"
                "model TEXT UNIQUE NOT NULL,"
                "name TEXT UNIQUE NOT NULL,"
                "cost TEXT,"
                "srp TEXT,"
                "stock INTEGER,"
                "rma INTEGER,"
                "rid INTEGER)")
            self.commitdb()
            query.exec_(
                "CREATE TABLE invoice ("
                "id INTEGER primary key AUTOINCREMENT,"
                "iv TEXT UNIQUE NOT NULL,"
                "da TEXT NOT NULL,"
                "bi TEXT NOT NULL,"
                "ad TEXT NOT NULL,"
                "at TEXT,"
                "te INTEGER,"
                "ci TEXT NOT NULL,"
                "du TEXT,"
                "sa TEXT,"
                "sl INTEGER,"
                "p1m TEXT,"
                "p1 TEXT,"
                "p1p INTEGER,"
                "p1c TEXT,"
                "p2m TEXT,"
                "p2 TEXT,"
                "p2p INTEGER,"
                "p2c TEXT,"
                "p3m TEXT,"
                "p3 TEXT,"
                "p3p INTEGER,"
                "p3c TEXT,"
                "p4m TEXT,"
                "p4 TEXT,"
                "p4p INTEGER,"
                "p4c TEXT,"
                "p5m TEXT,"
                "p5 TEXT,"
                "p5p INTEGER,"
                "p5c TEXT,"
                "p6m TEXT,"
                "p6 TEXT,"
                "p6p INTEGER,"
                "p6c TEXT,"
                "p7m TEXT,"
                "p7 TEXT,"
                "p7p INTEGER,"
                "p7c TEXT,"
                "p8m TEXT,"
                "p8 TEXT,"
                "p8p INTEGER,"
                "p8c TEXT,"
                "p9m TEXT,"
                "p9 TEXT,"
                "p9p INTEGER,"
                "p9c TEXT,"
                "p10m TEXT,"
                "p10 TEXT,"
                "p10p INTEGER,"
                "p10c TEXT,"
                "p11m TEXT,"
                "p11 TEXT,"
                "p11p INTEGER,"
                "p11c TEXT,"
                "p12m TEXT,"
                "p12 TEXT,"
                "p12p INTEGER,"
                "p12c TEXT,"
                "p13m TEXT,"
                "p13 TEXT,"
                "p13p INTEGER,"
                "p13c TEXT,"
                "p14m TEXT,"
                "p14 TEXT,"
                "p14p INTEGER,"
                "p14c TEXT,"
                "p15m TEXT,"
                "p15 TEXT,"
                "p15p INTEGER,"
                "p15c TEXT,"
                "p16m TEXT,"
                "p16 TEXT,"
                "p16p INTEGER,"
                "p16c TEXT,"
                "p17m TEXT,"
                "p17 TEXT,"
                "p17p INTEGER,"
                "p17c TEXT,"
                "p18m TEXT,"
                "p18 TEXT,"
                "p18p INTEGER,"
                "p18c TEXT,"
                "p19m TEXT,"
                "p19 TEXT,"
                "p19p INTEGER,"
                "p19c TEXT,"
                "p20m TEXT,"
                "p20 TEXT,"
                "p20p INTEGER,"
                "p20c TEXT,"
                "c1 TEXT,"
                "c2 TEXT,"
                "c3 TEXT,"
                "amount TEXT,"
                "pay TEXT)")
            self.commitdb()
            query.exec_(
                "CREATE TABLE inv_item_tmp ("
                "id INTEGER primary key AUTOINCREMENT,"
                "iv TEXT NOT NULL,"
                "p1m TEXT NOT NULL ,"
                "p1 TEXT NOT NULL,"
                "p1c TEXT NOT NULL,"
                "p1p INTEGER NOT NULL)")
            self.commitdb()
            query.exec_(
                "CREATE TABLE com_info ("
                "id INTEGER primary key AUTOINCREMENT,"
                "company TEXT ,"
                "addr TEXT )")
            self.commitdb()
            query.exec_(
                "CREATE TABLE bank_info ("
                "id INTEGER primary key AUTOINCREMENT,"
                "name TEXT ,"
                "code TEXT ,"
                "acc TEXT )")
            self.commitdb()
            query.exec_(
                "CREATE TABLE purchase ("
                "id INTEGER primary key AUTOINCREMENT,"
                "number_no TEXT UNIQUE NOT NULL,"
                "da TEXT NOT NULL,"
                "supplier TEXT NOT NULL,"
                "p1_name TEXT,"
                "p1_price TEXT,"
                "p1_qty INTEGER,"
                "p2_name TEXT,"
                "p2_price TEXT,"
                "p2_qty INTEGER,"
                "p3_name TEXT,"
                "p3_price TEXT,"
                "p3_qty INTEGER,"
                "p4_name TEXT,"
                "p4_price TEXT,"
                "p4_qty INTEGER,"
                "p5_name TEXT,"
                "p5_price TEXT,"
                "p5_qty INTEGER,"
                "p6_name TEXT,"
                "p6_price TEXT,"
                "p6_qty INTEGER,"
                "p7_name TEXT,"
                "p7_price TEXT,"
                "p7_qty INTEGER,"
                "p8_name TEXT,"
                "p8_price TEXT,"
                "p8_qty INTEGER,"
                "p9_name TEXT,"
                "p9_price TEXT,"
                "p9_qty INTEGER,"
                "p10_name TEXT,"
                "p10_price TEXT,"
                "p10_qty INTEGER,"
                "p11_name TEXT,"
                "p11_price TEXT,"
                "p11_qty INTEGER,"
                "p12_name TEXT,"
                "p12_price TEXT,"
                "p12_qty INTEGER,"
                "p13_name TEXT,"
                "p13_price TEXT,"
                "p13_qty INTEGER,"
                "p14_name TEXT,"
                "p14_price TEXT,"
                "p14_qty INTEGER,"
                "p15_name TEXT,"
                "p15_price TEXT,"
                "p15_qty INTEGER,"
                "p16_name TEXT,"
                "p16_price TEXT,"
                "p16_qty INTEGER,"
                "p17_name TEXT,"
                "p17_price TEXT,"
                "p17_qty INTEGER,"
                "p18_name TEXT,"
                "p18_price TEXT,"
                "p18_qty INTEGER,"
                "p19_name TEXT,"
                "p19_price TEXT,"
                "p19_qty INTEGER,"
                "p20_name TEXT,"
                "p20_price TEXT,"
                "p20_qty INTEGER,"
                "amount TEXT,"
                "qty INTEGER)")
            self.commitdb()
            query.exec_(
                "CREATE TABLE purchase_tmp ("
                "id INTEGER primary key AUTOINCREMENT,"
                "inv TEXT NOT NULL,"
                "pur_name TEXT UNIQUE NOT NULL,"
                "pur_pri TEXT NOT NULL,"
                "pur_qty INTEGER NOT NULL"
                ")")
            self.commitdb()
            query.exec_(
                "CREATE TABLE expense ("
                "id INTEGER primary key AUTOINCREMENT,"
                "iv TEXT UNIQUE NOT NULL,"
                "date TEXT NOT NULL,"
                "shop TEXT NOT NULL,"
                "n1 TEXT ,"
                "n1_price TEXT, "
                "n2 TEXT ,"
                "n2_price TEXT, "
                "n3 TEXT ,"
                "n3_price TEXT, "
                "n4 TEXT ,"
                "n4_price TEXT, "
                "n5 TEXT ,"
                "n5_price TEXT, "
                "n6 TEXT ,"
                "n6_price TEXT, "
                "n7 TEXT ,"
                "n7_price TEXT, "
                "n8 TEXT ,"
                "n8_price TEXT, "
                "n9 TEXT ,"
                "n9_price TEXT, "
                "n10 TEXT ,"
                "n10_price TEXT ,"
                "item TEXT NOT NULL,"
                "amount TEXT)")
            self.commitdb()
            query.exec_(
                "CREATE TABLE expense_tmp ("
                "id INTEGER primary key AUTOINCREMENT,"
                "inv TEXT NOT NULL,"
                "name TEXT UNIQUE NOT NULL,"
                "price TEXT NOT NULL"
                ")")
            self.commitdb()
            query.exec_(
                "CREATE TABLE cn ("
                "id INTEGER primary key AUTOINCREMENT,"
                "iv TEXT UNIQUE NOT NULL,"
                "da TEXT NOT NULL,"
                "bi TEXT NOT NULL,"
                "ad TEXT NOT NULL,"
                "at TEXT,"
                "te INTEGER,"
                "ci TEXT NOT NULL,"
                "du TEXT,"
                "sa TEXT,"
                "sl INTEGER,"
                "p1m TEXT,"
                "p1 TEXT,"
                "p1p INTEGER,"
                "p1c TEXT,"
                "p2m TEXT,"
                "p2 TEXT,"
                "p2p INTEGER,"
                "p2c TEXT,"
                "p3m TEXT,"
                "p3 TEXT,"
                "p3p INTEGER,"
                "p3c TEXT,"
                "p4m TEXT,"
                "p4 TEXT,"
                "p4p INTEGER,"
                "p4c TEXT,"
                "p5m TEXT,"
                "p5 TEXT,"
                "p5p INTEGER,"
                "p5c TEXT,"
                "p6m TEXT,"
                "p6 TEXT,"
                "p6p INTEGER,"
                "p6c TEXT,"
                "p7m TEXT,"
                "p7 TEXT,"
                "p7p INTEGER,"
                "p7c TEXT,"
                "p8m TEXT,"
                "p8 TEXT,"
                "p8p INTEGER,"
                "p8c TEXT,"
                "p9m TEXT,"
                "p9 TEXT,"
                "p9p INTEGER,"
                "p9c TEXT,"
                "p10m TEXT,"
                "p10 TEXT,"
                "p10p INTEGER,"
                "p10c TEXT,"
                "c1 TEXT,"
                "c2 TEXT,"
                "c3 TEXT,"
                "amount TEXT,"
                "clear TEXT)")
            self.commitdb()
            query.exec_(
                "CREATE TABLE cn_tmp ("
                "id INTEGER primary key AUTOINCREMENT,"
                "iv TEXT NOT NULL,"
                "p1m TEXT UNIQUE NOT NULL,"
                "p1 TEXT UNIQUE NOT NULL,"
                "p1c TEXT NOT NULL,"
                "p1p INTEGER NOT NULL)")
            self.commitdb()
            query.exec_(
                "CREATE TABLE client ("
                "id INTEGER primary key AUTOINCREMENT,"
                "name TEXT NOT NULL,"
                "ad TEXT NOT NULL,"
                "at TEXT NOT NULL,"
                "tel TEXT NOT NULL,"
                "ci TEXT UNIQUE NOT NULL)")
            self.commitdb()
            query.exec_(
                "CREATE TABLE return ("
                "id INTEGER primary key AUTOINCREMENT,"
                "iv TEXT UNIQUE NOT NULL,"
                "da TEXT NOT NULL,"
                "bi TEXT NOT NULL,"
                "ad TEXT NOT NULL,"
                "at TEXT,"
                "te INTEGER,"
                "ci TEXT NOT NULL,"
                "du TEXT,"
                "sa TEXT,"
                "sl INTEGER,"
                "p1m TEXT,"
                "p1 TEXT,"
                "p1p INTEGER,"
                "p1c TEXT,"
                "p2m TEXT,"
                "p2 TEXT,"
                "p2p INTEGER,"
                "p2c TEXT,"
                "p3m TEXT,"
                "p3 TEXT,"
                "p3p INTEGER,"
                "p3c TEXT,"
                "p4m TEXT,"
                "p4 TEXT,"
                "p4p INTEGER,"
                "p4c TEXT,"
                "p5m TEXT,"
                "p5 TEXT,"
                "p5p INTEGER,"
                "p5c TEXT,"
                "p6m TEXT,"
                "p6 TEXT,"
                "p6p INTEGER,"
                "p6c TEXT,"
                "p7m TEXT,"
                "p7 TEXT,"
                "p7p INTEGER,"
                "p7c TEXT,"
                "p8m TEXT,"
                "p8 TEXT,"
                "p8p INTEGER,"
                "p8c TEXT,"
                "p9m TEXT,"
                "p9 TEXT,"
                "p9p INTEGER,"
                "p9c TEXT,"
                "p10m TEXT,"
                "p10 TEXT,"
                "p10p INTEGER,"
                "p10c TEXT,"
                "p11m TEXT,"
                "p11 TEXT,"
                "p11p INTEGER,"
                "p11c TEXT,"
                "p12m TEXT,"
                "p12 TEXT,"
                "p12p INTEGER,"
                "p12c TEXT,"
                "p13m TEXT,"
                "p13 TEXT,"
                "p13p INTEGER,"
                "p13c TEXT,"
                "p14m TEXT,"
                "p14 TEXT,"
                "p14p INTEGER,"
                "p14c TEXT,"
                "p15m TEXT,"
                "p15 TEXT,"
                "p15p INTEGER,"
                "p15c TEXT,"
                "p16m TEXT,"
                "p16 TEXT,"
                "p16p INTEGER,"
                "p16c TEXT,"
                "p17m TEXT,"
                "p17 TEXT,"
                "p17p INTEGER,"
                "p17c TEXT,"
                "p18m TEXT,"
                "p18 TEXT,"
                "p18p INTEGER,"
                "p18c TEXT,"
                "p19m TEXT,"
                "p19 TEXT,"
                "p19p INTEGER,"
                "p19c TEXT,"
                "p20m TEXT,"
                "p20 TEXT,"
                "p20p INTEGER,"
                "p20c TEXT,"
                "c1 TEXT,"
                "c2 TEXT,"
                "c3 TEXT,"
                "amount TEXT)")
            self.commitdb()
            query.exec_(
                "CREATE TABLE ret_item_tmp ("
                "id INTEGER primary key AUTOINCREMENT,"
                "iv TEXT NOT NULL,"
                "p1m TEXT UNIQUE NOT NULL ,"
                "p1 TEXT UNIQUE NOT NULL,"
                "p1c TEXT NOT NULL,"
                "p1p INTEGER NOT NULL)")
            self.commitdb()
            self.add_comp_info()
            self.add_bank_info()
            self.closedb()
            print("Create table")

    def amprodco(self):
        self.total_cost = []
        self.proamcost = []
        self.proamstock = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT cost, stock FROM lib ")
            query.exec()
            while query.next():
                self.proamcost.append(decimal.Decimal(query.value(0)))
                self.proamstock.append(decimal.Decimal(query.value(1)))
            self.conn.commit()
            for a in range(len(self.proamcost)):
                co = self.proamcost[a]
                st = self.proamstock[a]
                self.totalcost = co * st
                self.total_cost.append(decimal.Decimal(self.totalcost))
            self.total_cost_sum = sum(self.total_cost)
            print("Total Product Cost")
            print(self.total_cost_sum)
            return self.total_cost_sum

    def amprodqty(self):
        self.total_qty = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT stock FROM lib ")
            query.exec()
            while query.next():
                self.total_qty.append(decimal.Decimal(query.value(0)))
            self.conn.commit()
            self.total_qtysum = sum(self.total_qty)
            print("Total Product QTY")
            print(self.total_qtysum)
            return self.total_qtysum

    def add_db(self, dbmodel, dbname, dbcost, dbsrp, dbstock, dbrma):
        if self.conn.open():
            #dbrid = self.pd_rid()
            query = QSqlQuery(self.conn)
            query.prepare("INSERT INTO lib (id,model,name,cost,srp,stock,rma)VALUES (NULL,?,?,?,?,?,?)")
            query.addBindValue(dbmodel)
            query.addBindValue(dbname)
            query.addBindValue(dbcost)
            query.addBindValue(dbsrp)
            query.addBindValue(dbstock)
            query.addBindValue(dbrma)
            #query.addBindValue(dbrid)
            query.exec()
            print("Add date")
            self.conn.commit()

    def updata_db(self, dbmodel, dbname, dbcost, dbsrp, dbstock, dbrma, dbid):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("UPDATE lib SET model=?,name=?,cost=?,srp=?,stock=?,rma=? WHERE id=? ")
            query.addBindValue(dbmodel)
            query.addBindValue(dbname)
            query.addBindValue(dbcost)
            query.addBindValue(dbsrp)
            query.addBindValue(dbstock)
            query.addBindValue(dbrma)
            query.addBindValue(dbid)
            query.exec()
            print("Upload_date")
            self.conn.commit()

    def delpro_db(self, model, name):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("DELETE FROM lib WHERE model=? and name =?")
            query.addBindValue(model)
            query.addBindValue(name)
            query.exec()
            print("Del_Product")
            self.conn.commit()

    def toconfirm_db(self, iv, mod, nam, pri, pcs):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("INSERT INTO inv_item_tmp (id,iv,p1m,p1,p1c,p1p)VALUES (NULL,?,?,?,?,?)")
            query.addBindValue(iv)
            query.addBindValue(mod)
            query.addBindValue(nam)
            query.addBindValue(pri)
            query.addBindValue(pcs)
            query.exec()
            print("Add confirm date")
            self.conn.commit()
           

    def del_conf_db(self,id):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("DELETE FROM inv_item_tmp WHERE id =?")
            query.addBindValue(id)
            query.exec()
            print("Del_conf_db")
            self.conn.commit()
            

    def inv_add_db_p1(self, iv, da, bi, ad, at, te, ci, du, sa, sl, c1, c2, c3, to_am):
        if self.conn.open():
            pay = "No"
            query = QSqlQuery(self.conn)
            query.prepare(
                "INSERT INTO invoice(id,iv,da,bi,ad,at,te,ci,du,sa,sl,c1,c2,c3,amount,pay)VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
            query.addBindValue(iv)
            query.addBindValue(da)
            query.addBindValue(bi)
            query.addBindValue(ad)
            query.addBindValue(at)
            query.addBindValue(te)
            query.addBindValue(ci)
            query.addBindValue(du)
            query.addBindValue(sa)
            query.addBindValue(sl)
            query.addBindValue(c1)
            query.addBindValue(c2)
            query.addBindValue(c3)
            query.addBindValue(to_am)
            query.addBindValue(pay)
            query.exec()
            print("inv_add_db")
            self.conn.commit()
            

    def capselect_db(self):
        self.results = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.exec_("SELECT iv, p1m, p1, p1c, p1p FROM inv_item_tmp")
            n = 0
            while query.next():
                self.results.append(query.value(0))
                self.results.append(query.value(1))
                self.results.append(query.value(2))
                self.results.append(query.value(3))
                self.results.append(query.value(4))
                n = n + 1
                if n == 20:
                    break
            self.conn.commit()
            #print(self.results)
            return self.results

    def excision_results(self,results,part):
        self.n = part
        self.output=[results[i:i + self.n] for i in range(0, len(results), self.n)]
        return self.output


    def upload_all_prod_inv(self,results):
        strqty = 1
        res = results
        if len(results) != 0:
            for step in range(len(res)):
                iv = res[step][0]
                pm = res[step][1]
                p = res[step][2]
                pc = res[step][3]
                pp = res[step][4]
                self.word = ("UPDATE invoice SET p","m=?,p","=?,p","c=?,p","p=? WHERE iv=?");
                self.sql= str(strqty).join(self.word);
                strqty = strqty + 1
                query = QSqlQuery(self.conn)
                query.prepare(self.sql)      
                query.addBindValue(pm)
                query.addBindValue(p)
                query.addBindValue(pc)
                query.addBindValue(pp)
                query.addBindValue(iv)
                query.exec()
                print("Upload prod db")
                self.conn.commit()         
            return iv,res


    def del_table(self):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.exec_("DELETE FROM inv_item_tmp")
            self.conn.commit()
            query.exec_("UPDATE sqlite_sequence SET SEQ = 0 WHERE NAME = 'inv_item_tmp'")
            self.conn.commit()
            

    def up_data(self,da,dua,inv):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("UPDATE invoice SET da=?,du=? WHERE iv=? ")
            query.addBindValue(da)
            query.addBindValue(dua)
            query.addBindValue(inv)
            query.exec()
            self.conn.commit()
            
    def inv_db(self, iv):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("DELETE FROM invoice WHERE iv =?")
            query.addBindValue(iv)
            query.exec()
            print("Del_inv")
            self.conn.commit()
            

    def tot_am(self):
        self.toam_results = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT p1c,p1p FROM inv_item_tmp ")
            query.exec()
            n = 0
            while query.next():
                pri = []
                qty = []
                pri.append(decimal.Decimal(query.value(0)))
                qty.append(decimal.Decimal(query.value(1)))
                n = n + 1
                if n == 21:
                    break
                pri_1 = pri[0]
                pri_2 = qty[0]
                pri_3 = pri_1 * pri_2
                self.toam_results.append(pri_3)
            total = sum(self.toam_results)
            print("total_am")
            self.conn.commit()
            return total

    def inv_tmpco(self):
        self.inv_tmpcount = None
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.exec_("SELECT count(*) FROM inv_item_tmp")
            while query.next():
                self.inv_tmpcount = query.value(0)
            self.conn.commit()
            return self.inv_tmpcount

    def select_prod_stock(self,res):
        self.stock = []
        self.items = res
        if self.conn.open():
            for step in range(len(self.items)):
                query = QSqlQuery(self.conn)
                query.prepare("SELECT model, stock FROM lib where model= ?")
                query.addBindValue(self.items[step][1])
                query.exec()
                while query.next():
                    self.stock.append(query.value(0))
                    self.stock.append(query.value(1))
                self.conn.commit()
            self.stock = self.excision_results(self.stock,2)
            print(self.stock)
            return self.stock

    def oneselect_prod_stock(self,res):
        self.stock = []
        self.items = res
        if self.conn.open():            
            query = QSqlQuery(self.conn)
            query.prepare("SELECT model, stock FROM lib where model= ?")
            query.addBindValue(self.items)
            query.exec()
            while query.next():
                self.stock.append(query.value(0))
                self.stock.append(query.value(1))
            self.conn.commit()
            print(self.stock)
            return self.stock

    def oneselect_conver_nametomodel(self,res):
        self.stock = []
        self.items = res
        if self.conn.open():            
            query = QSqlQuery(self.conn)
            query.prepare("SELECT name, stock FROM lib where name= ?")
            query.addBindValue(self.items)
            query.exec()
            while query.next():
                self.stock.append(query.value(0))
                self.stock.append(query.value(1))
            self.conn.commit()
            print(self.stock)
            return self.stock

    def upl_prodqty(self,res):
        if self.conn.open():
            for step in range(len(res)):
                self.item_model = res[step][1]
                self.item_sellout = res[step][4]
                self.stock = self.oneselect_prod_stock(self.item_model)
                self.lib_stock = self.stock[1]
                self.lib_prod = self.stock[0]
                self.renew = self.lib_stock - self.item_sellout
                print("Upload prod_stock")
                if (self.item_model == self.lib_prod):
                    query = QSqlQuery(self.conn)
                    query.prepare("UPDATE lib SET stock=? WHERE model=? ")
                    query.addBindValue(self.renew)
                    query.addBindValue(self.item_model)
                    query.exec()
                    self.conn.commit()

    def upload_toam(self,iv,am):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("UPDATE invoice SET amount=? WHERE iv=? ")
            query.addBindValue(am)
            query.addBindValue(iv)
            query.exec()
            self.conn.commit()

    def select_inv(self,iv):
        self.invinfo = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT * FROM invoice where iv= ?")
            query.addBindValue(iv)
            query.exec()
            while query.next():
                self.record = query.record().count()
                for index in range(self.record):
                    self.invinfo.append(query.value(index))
            self.conn.commit()
            return self.invinfo


    def delinv_stock(self,res):
        if self.conn.open():
            for step in range(len(res)):
                self.item_model = res[step][0]
                self.item_sellout = res[step][2]
                self.stock = self.oneselect_prod_stock(self.item_model) 
                self.lib_stock = self.stock[1]
                self.lib_prod = self.stock[0]
                self.renew = self.lib_stock + self.item_sellout
                print("Upload prod_stock")
                print(self.lib_stock)
                print(self.lib_prod)
                print(self.renew)
                if (self.item_model == self.lib_prod):
                    query = QSqlQuery(self.conn)
                    query.prepare("UPDATE lib SET stock=? WHERE model=? ")
                    query.addBindValue(self.renew)
                    query.addBindValue(self.item_model)
                    query.exec()
                    self.conn.commit()


    def pur_toconfirm_db(self, iv, nam, pri, qty):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("INSERT INTO purchase_tmp (id,inv,pur_name,pur_pri,pur_qty)VALUES (NULL,?,?,?,?)")
            query.addBindValue(iv)
            query.addBindValue(nam)
            query.addBindValue(pri)
            query.addBindValue(qty)
            query.exec()
            self.conn.commit()

    def pur_tmpco(self):
        self.pur_tmpcount = None
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.exec_("SELECT count(*) FROM purchase_tmp")
            while query.next():
                self.pur_tmpcount = query.value(0)
            self.conn.commit()
            return self.pur_tmpcount

    def pur_adddb(self, nu_no, da, sup, amount, qty):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("INSERT INTO purchase(id,number_no,da,supplier, amount, qty)VALUES (NULL,?,?,?,?,?)")
            query.addBindValue(nu_no)
            query.addBindValue(da)
            query.addBindValue(sup)
            query.addBindValue(amount)
            query.addBindValue(qty)
            query.exec()
            print("pur_add_db")
            self.conn.commit()

    def pur_capselect_db(self):
        self.pur_results = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.exec_("SELECT inv, pur_name, pur_pri, pur_qty FROM purchase_tmp")
            n = 0
            while query.next():
                self.pur_results.append(query.value(0))
                self.pur_results.append(query.value(1))
                self.pur_results.append(query.value(2))
                self.pur_results.append(query.value(3))
                n = n + 1
                if n == 20:
                    break
            self.conn.commit()
            return self.pur_results

    def tot_pur_am(self):
        self.toam_results = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT pur_pri,pur_qty FROM purchase_tmp ")
            query.exec()
            n = 0
            while query.next():
                pri = []
                qty = []
                pri.append(query.value(0))
                qty.append(query.value(1))
                n = n + 1
                if n == 21:
                    break
                pri_1 = decimal.Decimal(str(pri[0]))
                pri_2 = decimal.Decimal(str(qty[0]))
                pri_3 = pri_1 * pri_2
                self.toam_results.append(pri_3)
            self.total = sum(self.toam_results)
            self.conn.commit()
            return self.total

    def tot_pur_qty(self):
        self.toqty_results = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT pur_qty FROM purchase_tmp ")
            query.exec()
            n = 0
            while query.next():
                self.toqty_results.append(decimal.Decimal(query.value(0)))
                n = n + 1
                if n == 20:
                    break
            self.toqty_pur = sum(self.toqty_results)
            self.conn.commit()
            return self.toqty_pur

    def upload_all_prod_pur(self,results):
        strqty = 1
        res = results
        if len(results) != 0:
            for step in range(len(res)):
                iv = res[step][0]
                na = res[step][1]
                pri = res[step][2]
                qty = res[step][3]
                self.word = ("UPDATE purchase SET p","_name=?,p","_price=?,p","_qty=? WHERE number_no=? ");
                self.sql= str(strqty).join(self.word);
                strqty = strqty + 1
                query = QSqlQuery(self.conn)
                query.prepare(self.sql)      
                query.addBindValue(na)
                query.addBindValue(pri)
                query.addBindValue(qty)
                query.addBindValue(iv)
                query.exec()
                print("Upload prod db")
                self.conn.commit()         
            return iv,res

    def del_pur_table(self):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.exec_("DELETE FROM purchase_tmp")
            print("Del_pur_table db")
            self.conn.commit()
            query.exec_("UPDATE sqlite_sequence SET SEQ = 0 WHERE NAME = 'purchase_tmp'")
            print("UpL_sqlite_sequence db")
            self.conn.commit()

    def up_pur_data(self,da,inv):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("UPDATE purchase SET da=? WHERE number_no=? ")
            query.addBindValue(da)
            query.addBindValue(inv)
            query.exec()
            print("UpL_Data db")
            self.conn.commit()


    def upl_purdqty(self,res):
        print("----!!!!!!!!!-----")
        if self.conn.open():
            for step in range(len(res)):
                self.item_name = res[step][1]
                self.item_price = res[step][2]
                self.item_purqty = res[step][3]
                self.stock = self.oneselect_conver_nametomodel(self.item_name)
                self.lib_stock = self.stock[1]
                self.lib_name = self.stock[0]
                self.renew = self.lib_stock + self.item_purqty
                print("Upload prod_stock")
                print("-------------")
                print(self.lib_stock)
                print(self.lib_name)
                print(self.renew)
                if (self.item_name == self.lib_name):
                    query = QSqlQuery(self.conn)
                    query.prepare("UPDATE lib SET stock=?,cost=? WHERE name=? ")
                    query.addBindValue(self.renew)
                    query.addBindValue(self.item_price)
                    query.addBindValue(self.item_name)
                    query.exec()
                    self.conn.commit()

    def select_pur(self,iv):
        self.purinfo = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT * FROM purchase where number_no= ?")
            query.addBindValue(iv)
            query.exec()
            while query.next():
                self.record = query.record().count()
                for index in range(self.record):
                    self.purinfo.append(query.value(index))
            self.conn.commit()
            return self.purinfo

    def delpur_stock(self,res):
        if self.conn.open():
            for step in range(len(res)):
                self.item_name = res[step][0]
                self.item_purout = res[step][2]
                self.stock = self.oneselect_conver_nametomodel(self.item_name) 
                self.lib_prod = self.stock[0]
                self.lib_stock = self.stock[1]
                self.renew = self.lib_stock - self.item_purout
                print("Upload prod_stock")
                print(self.lib_stock)
                print(self.lib_prod)
                print(self.renew)
                if (self.item_name == self.lib_prod):
                    query = QSqlQuery(self.conn)
                    query.prepare("UPDATE lib SET stock=? WHERE name=? ")
                    query.addBindValue(self.renew)
                    query.addBindValue(self.item_name)
                    query.exec()
                    self.conn.commit()    


    def del_purdb(self, iv):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("DELETE FROM purchase WHERE number_no =?")
            query.addBindValue(iv)
            query.exec()
            self.conn.commit()

    def del_pur_conf_db(self, na):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("DELETE FROM purchase_tmp WHERE pur_name =?")
            query.addBindValue(na)
            query.exec()
            self.conn.commit()

    def upl_exp_db(self, inv, name, price):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("INSERT INTO expense_tmp (id,inv,name,price)VALUES (NULL,?,?,?)")
            query.addBindValue(inv)
            query.addBindValue(name)
            query.addBindValue(price)
            query.exec()
            print("Add exp_data")
            self.conn.commit()

    def exp_tmpco(self):
        self.exp_tmpcount = None
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.exec_("SELECT count(*) FROM expense_tmp")
            while query.next():
                self.exp_tmpcount = query.value(0)
            print(self.exp_tmpcount)
            self.conn.commit()
            return self.exp_tmpcount

    def upl_all_exp_db(self, inv, da, sh, cm, to_am):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("INSERT INTO expense (id,iv,date,shop,item,amount)VALUES (NULL,?,?,?,?,?)")
            query.addBindValue(inv)
            query.addBindValue(da)
            query.addBindValue(sh)
            query.addBindValue(cm)
            query.addBindValue(to_am)
            query.exec()
            print("Add exp_alldata")
            self.conn.commit()

    def exp_capselect_db(self):
        self.exp_results = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.exec_("SELECT inv, name, price FROM expense_tmp")
            n = 0
            while query.next():
                self.exp_results.append(query.value(0))
                self.exp_results.append(query.value(1))
                self.exp_results.append(query.value(2))
                n = n + 1
                if n == 10:
                    break
            #print(self.exp_results)
            self.conn.commit()
            return self.exp_results

    def upload_all_prod_exp(self,results):
        strqty = 1
        res = results
        if len(results) != 0:
            print(len(res))
            for step in range(len(res)):
                iv = res[step][0]
                na = res[step][1]
                pri = res[step][2]
                self.word = ("UPDATE expense SET n","=?,n","_price=? WHERE iv=?");
                self.sql= str(strqty).join(self.word);
                print(self.sql)
                strqty = strqty + 1
                query = QSqlQuery(self.conn)
                query.prepare(self.sql)      
                query.addBindValue(na)
                query.addBindValue(pri)
                query.addBindValue(iv)
                query.exec()
                print("Upload exp db")
                self.conn.commit()         

    def tot_exp_am(self):
        self.toam_results = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT price FROM expense_tmp ")
            query.exec()
            n = 0
            while query.next():
                pri = []
                pri.append(query.value(0))
                n = n + 1
                if n == 11:
                    break
                pri_1 = decimal.Decimal(str(pri[0]))
                self.toam_results.append(pri_1)
            total = sum(self.toam_results)
            print("total_am")
            self.conn.commit()
            return total

    def del_exp_db(self, na):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("DELETE FROM expense_tmp WHERE name =?")
            query.addBindValue(na)
            query.exec()
            print("del_exp_db")
            self.conn.commit()

    def del_exp_table(self):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.exec_("DELETE FROM expense_tmp")
            print("Del_exp_table db")
            self.conn.commit()
            query.exec_("UPDATE sqlite_sequence SET SEQ = 0 WHERE NAME = 'expense_tmp'")
            print("UpL_sqlite_sequence db")
            self.conn.commit()

    def del_expdb(self, iv):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("DELETE FROM expense WHERE iv =?")
            query.addBindValue(iv)
            query.exec()
            print("Del_exp")
            self.conn.commit()

    def up_exp_data(self,da,inv):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            print(da)
            print(inv)
            query.prepare("UPDATE expense SET date=? WHERE iv=? ")
            query.addBindValue(da)
            query.addBindValue(inv)
            query.exec()
            print("UpL_Data db")
            self.conn.commit()


    def upl_cn_db(self, inv, model, des, price, qty):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("INSERT INTO cn_tmp (id,iv,p1m,p1,p1c,p1p)VALUES (NULL,?,?,?,?,?)")
            query.addBindValue(inv)
            query.addBindValue(model)
            query.addBindValue(des)
            query.addBindValue(price)
            query.addBindValue(qty)
            query.exec()
            self.conn.commit()

    def cn_tmpco(self):
        self.cn_tmpcount = None
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.exec_("SELECT count(*) FROM cn_tmp")
            while query.next():
                self.cn_tmpcount = query.value(0)
            print(self.cn_tmpcount)
            self.conn.commit()
            return self.cn_tmpcount

    def del_cntmp_db(self, na):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("DELETE FROM cn_tmp WHERE p1 =?")
            query.addBindValue(na)
            query.exec()
            print("del_cn_db")
            self.conn.commit()

    def cn_add_db_p1(self, iv, da, bi, ad, at, te, ci, du, sa, sl, c1, c2, c3, amount):
        if self.conn.open():
            clear = "No"
            query = QSqlQuery(self.conn)
            query.prepare(
                "INSERT INTO cn(id,iv,da,bi,ad,at,te,ci,du,sa,sl,c1,c2,c3,amount,clear)VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
            query.addBindValue(iv)
            query.addBindValue(da)
            query.addBindValue(bi)
            query.addBindValue(ad)
            query.addBindValue(at)
            query.addBindValue(te)
            query.addBindValue(ci)
            query.addBindValue(du)
            query.addBindValue(sa)
            query.addBindValue(sl)
            query.addBindValue(c1)
            query.addBindValue(c2)
            query.addBindValue(c3)
            query.addBindValue(amount)
            query.addBindValue(clear)
            query.exec()
            print("cn_add_db")
            self.conn.commit()

    def cn_capselect_db(self):
        self.cn_results = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.exec_("SELECT iv, p1m, p1, p1c, p1p FROM cn_tmp")
            n = 0
            while query.next():
                self.cn_results.append(query.value(0))
                self.cn_results.append(query.value(1))
                self.cn_results.append(query.value(2))
                self.cn_results.append(query.value(3))
                self.cn_results.append(query.value(4))
                n = n + 1
                if n == 10:
                    break
            self.conn.commit()
            return self.cn_results

    def upload_all_prod_cn(self,results):
        strqty = 1
        res = results
        if len(results) != 0:
            for step in range(len(res)):
                iv = res[step][0]
                pm = res[step][1]
                p = res[step][2]
                pc = res[step][3]
                pp = res[step][4]
                self.word = ("UPDATE cn SET p","m=?,p","=?,p","c=?,p","p=? WHERE iv=?");
                self.sql= str(strqty).join(self.word);
                strqty = strqty + 1
                query = QSqlQuery(self.conn)
                query.prepare(self.sql)      
                query.addBindValue(pm)
                query.addBindValue(p)
                query.addBindValue(pc)
                query.addBindValue(pp)
                query.addBindValue(iv)
                query.exec()
                print("Upload prod db")
                self.conn.commit()         
            return iv,res

    def tot_cn_am(self):
        self.toam_results = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT p1c,p1p FROM cn_tmp ")
            query.exec()
            n = 0
            while query.next():
                pri = []
                qty = []
                pri.append(query.value(0))
                qty.append(query.value(1))
                n = n + 1
                if n == 11:
                    break
                pri_1 = decimal.Decimal(str(pri[0]))
                pri_2 = decimal.Decimal(str(qty[0]))
                pri_3 = pri_1 * pri_2
                self.toam_results.append(pri_3)
            self.total = sum(self.toam_results)
            print("total_pur_am")
            self.conn.commit()
            return self.total

    def cnuplpaym_db(self, inv_nu, pay_st):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("UPDATE cn SET clear=? WHERE iv=? ")
            query.addBindValue(pay_st)
            query.addBindValue(inv_nu)
            query.exec()
            print("Upload CN Payment date")
            self.conn.commit()

    def up_cn_data(self,da,dua,inv):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("UPDATE cn SET da=?,du=? WHERE iv=? ")
            query.addBindValue(da)
            query.addBindValue(dua)
            query.addBindValue(inv)
            query.exec()
            print("UpL_Data db")
            self.conn.commit()

    def del_cn_table(self):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.exec_("DELETE FROM cn_tmp")
            print("Del_cn_table db")
            self.conn.commit()
            query.exec_("UPDATE sqlite_sequence SET SEQ = 0 WHERE NAME = 'cn_tmp'")
            print("UpL_sqlite_sequence db")
            self.conn.commit()

    def del_cn_db(self, iv):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("DELETE FROM cn WHERE iv =?")
            query.addBindValue(iv)
            query.exec()
            print("Del_cn")
            self.conn.commit()

    def cheq_search(self, da_st, da_du):
        self.cheq_results = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT iv, da, ci, du, amount, pay FROM invoice WHERE da BETWEEN ? and ? ")
            query.addBindValue(da_st)
            query.addBindValue(da_du)
            query.exec()
            while query.next():
                self.cheq_results.append(query.value(0))
                self.cheq_results.append(query.value(1))
                self.cheq_results.append(query.value(2))
                self.cheq_results.append(query.value(3))
                self.cheq_results.append(query.value(4))
                self.cheq_results.append(query.value(5))
            print("Search_Cheq")
            self.conn.commit()
            return self.cheq_results

    def chequplpaym_db(self, inv_nu, namci, pay_st):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("UPDATE invoice SET pay=? WHERE iv=? and ci=? ")
            query.addBindValue(pay_st)
            query.addBindValue(inv_nu)
            query.addBindValue(namci)
            query.exec()
            print("Upload payment date")
            self.conn.commit()

    def cheqinvsearch_db(self, inv_ed):
        self.cheqinv_results = []
        inv_edp2 = "%" + inv_ed + "%"
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT iv, da, ci, du, amount, pay FROM invoice WHERE iv like ?")
            query.addBindValue(inv_edp2)
            query.exec()
            while query.next():
                self.cheqinv_results.append(query.value(0))
                self.cheqinv_results.append(query.value(1))
                self.cheqinv_results.append(query.value(2))
                self.cheqinv_results.append(query.value(3))
                self.cheqinv_results.append(query.value(4))
                self.cheqinv_results.append(query.value(5))
            print("Search_Cheq")
            self.conn.commit()
            return self.cheqinv_results

    def chequnpaid_search(self):
        self.unpaid_results = []
        self.pay = "No"
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT iv, da, ci, du, amount, pay FROM invoice WHERE pay=? ")
            query.addBindValue(self.pay)
            query.exec()
            while query.next():
                self.unpaid_results.append(query.value(0))
                self.unpaid_results.append(query.value(1))
                self.unpaid_results.append(query.value(2))
                self.unpaid_results.append(query.value(3))
                self.unpaid_results.append(query.value(4))
                self.unpaid_results.append(query.value(5))
            print("Search_Cheq")
            self.conn.commit()
            return self.unpaid_results

    def cn_search(self, da_st, da_du):
        self.cn_sear_results = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT iv, da, ci, amount, clear FROM cn WHERE da BETWEEN ? and ? ")
            query.addBindValue(da_st)
            query.addBindValue(da_du)
            query.exec()
            while query.next():
                self.cn_sear_results.append(query.value(0))
                self.cn_sear_results.append(query.value(1))
                self.cn_sear_results.append(query.value(2))
                self.cn_sear_results.append(query.value(3))
                self.cn_sear_results.append(query.value(4))
            print("Search_cn")
            self.conn.commit()
            return self.cn_sear_results

    def cn_uplpaym_db(self, cn_nu, namci, pay_st):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("UPDATE cn SET clear=? WHERE iv=? and ci=? ")
            query.addBindValue(pay_st)
            query.addBindValue(cn_nu)
            query.addBindValue(namci)
            query.exec()
            print("Upload payment date")
            self.conn.commit()

    def cninvsearch_db(self, cn_ed):
        self.cninv_results = []
        cn_edp2 = "%" + cn_ed + "%"
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT iv, da, ci, amount, clear FROM cn WHERE iv like ?")
            query.addBindValue(cn_edp2)
            query.exec()
            while query.next():
                self.cninv_results.append(query.value(0))
                self.cninv_results.append(query.value(1))
                self.cninv_results.append(query.value(2))
                self.cninv_results.append(query.value(3))
                self.cninv_results.append(query.value(4))
            # print(self.cheq_results)
            print("Search_cn")
            self.conn.commit()
            return self.cninv_results

    def cn_unpaid_search(self):
        self.cnunpaid_search = []
        self.cn_pay = "No"
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT iv, da, ci, amount, clear FROM cn WHERE clear=? ")
            query.addBindValue(self.cn_pay)
            query.exec()
            while query.next():
                self.cnunpaid_search.append(query.value(0))
                self.cnunpaid_search.append(query.value(1))
                self.cnunpaid_search.append(query.value(2))
                self.cnunpaid_search.append(query.value(3))
                self.cnunpaid_search.append(query.value(4))
            print(self.cnunpaid_search)
            print("Search_Cheq")
            self.conn.commit()
            return self.cnunpaid_search

    def report_inv_dl(self, da_st, da_du):
        self.re_da = []
        self.re_iv = []
        self.re_ci = []
        self.re_am = []
        self.re_du = []
        self.re_pay = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT da, iv, ci, amount,du, pay FROM invoice WHERE da BETWEEN ? and ? ")
            query.addBindValue(da_st)
            query.addBindValue(da_du)
            query.exec()
            while query.next():
                self.re_da.append(query.value(0))
                self.re_iv.append(query.value(1))
                self.re_ci.append(query.value(2))
                self.re_am.append(query.value(3))
                self.re_du.append(query.value(4))
                self.re_pay.append(query.value(5))
            print("Search_report")
            self.conn.commit()
            return self.re_da, self.re_iv, self.re_ci, self.re_am, self.re_du, self.re_pay

    def report_exp_dl(self, da_st, da_du):
        self.reex_da = []
        self.reex_iv = []
        self.reex_sh = []
        self.reex_am = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT date, iv,shop, amount FROM expense WHERE date BETWEEN ? and ? ")
            query.addBindValue(da_st)
            query.addBindValue(da_du)
            query.exec()
            while query.next():
                self.reex_da.append(query.value(0))
                self.reex_iv.append(query.value(1))
                self.reex_sh.append(query.value(2))
                self.reex_am.append(query.value(3))
            print("Searchex_report")
            self.conn.commit()
            return self.reex_da, self.reex_iv, self.reex_sh, self.reex_am

    def report_pur_dl(self, da_st, da_du):
        self.repu_da = []
        self.repu_iv = []
        self.repu_su = []
        self.repu_am = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT da, number_no, supplier, amount FROM purchase WHERE da BETWEEN ? and ? ")
            query.addBindValue(da_st)
            query.addBindValue(da_du)
            query.exec()
            while query.next():
                self.repu_da.append(query.value(0))
                self.repu_iv.append(query.value(1))
                self.repu_su.append(query.value(2))
                self.repu_am.append(query.value(3))
            print("Searchpur_report")
            self.conn.commit()
            return self.repu_da, self.repu_iv, self.repu_su, self.repu_am

    def report_cn_dl(self, da_st, da_du):
        self.recn_da = []
        self.recn_iv = []
        self.recn_sh = []
        self.recn_am = []
        self.recn_clear = []

        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT da, iv, ci, amount,clear FROM cn WHERE da BETWEEN ? and ? ")
            query.addBindValue(da_st)
            query.addBindValue(da_du)
            query.exec()
            while query.next():
                self.recn_da.append(query.value(0))
                self.recn_iv.append(query.value(1))
                self.recn_sh.append(query.value(2))
                self.recn_am.append(query.value(3))
                self.recn_clear.append(query.value(4))
            print("Searchcn_report")
            self.conn.commit()
            return self.recn_da, self.recn_iv, self.recn_sh, self.recn_am, self.recn_clear

    def report_ret_dl(self, da_st, da_du):
        self.reret_da = []
        self.reret_iv = []
        self.reret_sh = []
        self.reret_am = []

        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT da, iv, ci, amount FROM return WHERE da BETWEEN ? and ? ")
            query.addBindValue(da_st)
            query.addBindValue(da_du)
            query.exec()
            while query.next():
                self.reret_da.append(query.value(0))
                self.reret_iv.append(query.value(1))
                self.reret_sh.append(query.value(2))
                self.reret_am.append(query.value(3))
            print("Searchret_report")
            self.conn.commit()
            return self.reret_da, self.reret_iv, self.reret_sh, self.reret_am

    def client_add_db(self, client_na, client_ad, client_at, client_tel, client_ci):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("INSERT INTO client (id,name,ad,at,tel,ci)VALUES (NULL,?,?,?,?,?)")
            query.addBindValue(client_na)
            query.addBindValue(client_ad)
            query.addBindValue(client_at)
            query.addBindValue(client_tel)
            query.addBindValue(client_ci)
            query.exec()
            print("Add date")
            self.conn.commit()

    def client_updata_db(self, client_na, client_ad, client_at, client_tel, client_ci, dbid):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("UPDATE client SET name=?,ad=?,at=?,tel=?,ci=? WHERE id=? ")
            query.addBindValue(client_na)
            query.addBindValue(client_ad)
            query.addBindValue(client_at)
            query.addBindValue(client_tel)
            query.addBindValue(client_ci)
            query.addBindValue(dbid)
            query.exec()
            print("Upload")
            self.conn.commit()

    def client_delpro_db(self, client_na, client_ad):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("DELETE FROM client WHERE name=? and ad =?")
            query.addBindValue(client_na)
            query.addBindValue(client_ad)
            query.exec()
            print("Del_Product")
            self.conn.commit()

    def pl_exp_rep(self, da_st, da_du, item):
        self.re_am = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT amount FROM expense WHERE item=? and date BETWEEN ? and ? ")
            query.addBindValue(item)
            query.addBindValue(da_st)
            query.addBindValue(da_du)
            query.exec()
            while query.next():
                self.re_am.append(decimal.Decimal(query.value(0)))
            print("Search_pl_report")
            self.conn.commit()
            self.re_am = sum(self.re_am)
            print(self.re_am)
            return self.re_am

    def pl_pur_rep(self, da_st, da_du):
        self.re_pur_am = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT amount FROM purchase WHERE da BETWEEN ? and ? ")
            query.addBindValue(da_st)
            query.addBindValue(da_du)
            query.exec()
            while query.next():
                self.re_pur_am.append(decimal.Decimal(query.value(0)))
            print("Search_pl_report")
            self.conn.commit()
            self.re_pur_am = sum(self.re_pur_am)
            print(self.re_pur_am)
            return self.re_pur_am

    def pl_inv_rep(self, da_st, da_du):
        self.re_inv_am = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT amount FROM invoice WHERE da BETWEEN ? and ? ")
            query.addBindValue(da_st)
            query.addBindValue(da_du)
            query.exec()
            while query.next():
                self.re_inv_am.append(decimal.Decimal(query.value(0)))
            print("Search_pl_report")
            self.conn.commit()
            self.re_inv_am = sum(self.re_inv_am)
            print(self.re_inv_am)
            return self.re_inv_am

    def pl_cn_rep(self, da_st, da_du):
        self.re_cn_am = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT amount FROM cn WHERE da BETWEEN ? and ? ")
            query.addBindValue(da_st)
            query.addBindValue(da_du)
            query.exec()
            while query.next():
                self.re_cn_am.append(decimal.Decimal(query.value(0)))
            print("Search_pl_report")
            self.conn.commit()
            self.re_cn_am = sum(self.re_cn_am)
            print(self.re_cn_am)
            return self.re_cn_am

    def bank_info(self, na, co, ac):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("UPDATE bank_info SET name=?,code=?,acc=? WHERE id=1 ")
            query.addBindValue(na)
            query.addBindValue(co)
            query.addBindValue(ac)
            query.exec()
            print("Upload_Comp_info")
            self.conn.commit()

    def add_bank_info(self):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("INSERT INTO bank_info (id,name,code,acc)VALUES (1,?,?,?)")
            query.addBindValue("Company Name")
            query.addBindValue("Bank Code")
            query.addBindValue("Bank Acc")
            query.exec()
            print("Upload")
            self.conn.commit()

    def display_bankinfo(self):
        self.bankinfo = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.exec_("SELECT * FROM bank_info")
            while query.next():
                self.bankinfo.append(query.value(0))
                self.bankinfo.append(query.value(1))
                self.bankinfo.append(query.value(2))
                self.bankinfo.append(query.value(3))
            return self.bankinfo

    def comp_info(self, cn, ca):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("UPDATE com_info SET company=?,addr=? WHERE id=1 ")
            query.addBindValue(cn)
            query.addBindValue(ca)
            query.exec()
            print("Upload_Comp_info")
            self.conn.commit()

    def add_comp_info(self):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("INSERT INTO com_info (id,company,addr)VALUES (1,?,?)")
            query.addBindValue("Company Name")
            query.addBindValue("Company Address")
            query.exec()
            print("Upload")
            self.conn.commit()

    def display_cominfo(self):
        self.cominfo = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.exec_("SELECT * FROM com_info")
            while query.next():
                self.cominfo.append(query.value(0))
                self.cominfo.append(query.value(1))
                self.cominfo.append(query.value(2))
            return self.cominfo

    def check_purnum(self, num):
        self.checkinfo = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT number_no FROM purchase where number_no = ?")
            query.addBindValue(num)
            query.exec()
            while query.next():
                self.checkinfo.append(query.value(0))
            self.conn.commit()
            return self.checkinfo

    def check_invnum(self, num):
        self.checkinfo = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT iv FROM invoice where iv = ?")
            query.addBindValue(num)
            query.exec()
            while query.next():
                self.checkinfo.append(query.value(0))
            self.conn.commit()
            return self.checkinfo

    def check_cnnum(self, num):
        self.checkinfo = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT iv FROM cn where iv = ?")
            query.addBindValue(num)
            query.exec()
            while query.next():
                self.checkinfo.append(query.value(0))
            self.conn.commit()
            return self.checkinfo

    def check_expnum(self, num):
        self.checkinfo = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT iv FROM expense where iv = ?")
            query.addBindValue(num)
            query.exec()
            while query.next():
                self.checkinfo.append(query.value(0))
            self.conn.commit()
            return self.checkinfo

    def check_retnum(self, num):
        self.checkinfo = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT iv FROM return where iv = ?")
            query.addBindValue(num)
            query.exec()
            while query.next():
                self.checkinfo.append(query.value(0))
            self.conn.commit()
            return self.checkinfo

    def ret_add_db_p1(self, iv, da, bi, ad, at, te, ci, du, sa, sl, c1, c2, c3, to_am):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare(
                "INSERT INTO return(id,iv,da,bi,ad,at,te,ci,du,sa,sl,c1,c2,c3,amount)VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
            query.addBindValue(iv)
            query.addBindValue(da)
            query.addBindValue(bi)
            query.addBindValue(ad)
            query.addBindValue(at)
            query.addBindValue(te)
            query.addBindValue(ci)
            query.addBindValue(du)
            query.addBindValue(sa)
            query.addBindValue(sl)
            query.addBindValue(c1)
            query.addBindValue(c2)
            query.addBindValue(c3)
            query.addBindValue(to_am)
            query.exec()
            print("ret_add_db")
            self.conn.commit()

    def retcapselect_db(self):
        self.ret_results = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.exec_("SELECT iv, p1m, p1, p1c, p1p FROM ret_item_tmp")
            n = 0
            while query.next():
                self.ret_results.append(query.value(0))
                self.ret_results.append(query.value(1))
                self.ret_results.append(query.value(2))
                self.ret_results.append(query.value(3))
                self.ret_results.append(query.value(4))
                n = n + 1
                if n == 20:
                    break
            self.conn.commit()
            return self.ret_results

    def upload_all_prod_ret(self,results):
        strqty = 1
        res = results
        if len(results) != 0:
            for step in range(len(res)):
                iv = res[step][0]
                pm = res[step][1]
                p = res[step][2]
                pc = res[step][3]
                pp = res[step][4]
                self.word = ("UPDATE return SET p","m=?,p","=?,p","c=?,p","p=? WHERE iv=?");
                self.sql= str(strqty).join(self.word);
                strqty = strqty + 1
                query = QSqlQuery(self.conn)
                query.prepare(self.sql)      
                query.addBindValue(pm)
                query.addBindValue(p)
                query.addBindValue(pc)
                query.addBindValue(pp)
                query.addBindValue(iv)
                query.exec()
                print("Upload prod db")
                self.conn.commit()         
            return iv,res


    def upl_retprodqty(self,res):
        if self.conn.open():
            for step in range(len(res)):
                self.item_model = res[step][1]
                self.item_sellout = res[step][4]
                self.stock = self.oneselect_prod_stock(self.item_model)
                self.lib_stock = self.stock[1]
                self.lib_prod = self.stock[0]
                self.renew = self.lib_stock + self.item_sellout
                if (self.item_model == self.lib_prod):
                    query = QSqlQuery(self.conn)
                    query.prepare("UPDATE lib SET stock=? WHERE model=? ")
                    query.addBindValue(self.renew)
                    query.addBindValue(self.item_model)
                    query.exec()
                    self.conn.commit()


    def rettot_am(self):
        self.toam_results = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT p1c,p1p FROM ret_item_tmp ")
            query.exec()
            n = 0
            while query.next():
                pri = []
                qty = []
                pri.append(decimal.Decimal(query.value(0)))
                qty.append(decimal.Decimal(query.value(1)))
                n = n + 1
                if n == 21:
                    break
                pri_1 = pri[0]
                pri_2 = qty[0]
                pri_3 = pri_1 * pri_2
                self.toam_results.append(pri_3)
            total = sum(self.toam_results)
            print("total_am")
            self.conn.commit()
            return total

    def del_ret_table(self):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.exec_("DELETE FROM ret_item_tmp")
            print("Del_table db")
            self.conn.commit()
            query.exec_("UPDATE sqlite_sequence SET SEQ = 0 WHERE NAME = 'ret_item_tmp'")
            print("UpL_sqlite_sequence db")
            self.conn.commit()

    def ret_toconfirm_db(self, iv, mod, nam, pri, pcs):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("INSERT INTO ret_item_tmp (id,iv,p1m,p1,p1c,p1p)VALUES (NULL,?,?,?,?,?)")
            query.addBindValue(iv)
            query.addBindValue(mod)
            query.addBindValue(nam)
            query.addBindValue(pri)
            query.addBindValue(pcs)
            query.exec()
            print("Add confirm date")
            self.conn.commit()

    def ret_tmpco(self):
        self.ret_tmpcount = None
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.exec_("SELECT count(*) FROM ret_item_tmp")
            while query.next():
                self.ret_tmpcount = query.value(0)
            print(self.ret_tmpcount)
            self.conn.commit()
            return self.ret_tmpcount

    def del_ret_conf_db(self, na, idp):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("DELETE FROM ret_item_tmp WHERE p1m =? and id =?")
            query.addBindValue(na)
            query.addBindValue(idp)
            query.exec()
            print("del_conf_db")
            self.conn.commit()

    def select_ret(self,iv):
        self.invinfo = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT * FROM return where iv= ?")
            query.addBindValue(iv)
            query.exec()
            while query.next():
                self.record = query.record().count()
                for index in range(self.record):
                    self.invinfo.append(query.value(index))
            self.conn.commit()
            print(self.invinfo)
            return self.invinfo

    def delret_stock(self,res):
        if self.conn.open():
            for step in range(len(res)):
                self.item_model = res[step][0]
                self.item_sellout = res[step][2]
                self.stock = self.oneselect_prod_stock(self.item_model) 
                self.lib_stock = self.stock[1]
                self.lib_prod = self.stock[0]
                self.renew = self.lib_stock - self.item_sellout
                print("Upload prod_stock")
                print(self.lib_stock)
                print(self.lib_prod)
                print(self.renew)
                if (self.item_model == self.lib_prod):
                    query = QSqlQuery(self.conn)
                    query.prepare("UPDATE lib SET stock=? WHERE model=? ")
                    query.addBindValue(self.renew)
                    query.addBindValue(self.item_model)
                    query.exec()
                    self.conn.commit()

    def ret_db(self, iv):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("DELETE FROM return WHERE iv =?")
            query.addBindValue(iv)
            query.exec()
            print("Del_ret")
            self.conn.commit()

    def up_ret_data(self,da,dua,inv):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            print(da)
            print(dua)
            print(inv)
            query.prepare("UPDATE return SET da=?,du=? WHERE iv=? ")
            query.addBindValue(da)
            query.addBindValue(dua)
            query.addBindValue(inv)
            query.exec()
            print("UpL_Data db")
            self.conn.commit()

    def pur_sup_list(self):
        self.purlist = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT supplier FROM purchase GROUP BY supplier ORDER BY supplier ")
            query.exec()
            while query.next():
                self.purlist.append(query.value(0))
            self.conn.commit()
            return self.purlist

    def exp_sup_list(self):
        self.exp_list = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT shop FROM expense GROUP BY shop ORDER BY shop ")
            query.exec()
            while query.next():
                self.exp_list.append(query.value(0))
            self.conn.commit()
            return self.exp_list

    def sell_out_search(self, da_st, da_du,text):
        self.sell_out_results = []
        edp2 = "%" + text + "%"
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT iv, da, ci, du, amount, pay FROM invoice WHERE da BETWEEN ? and ? "
                          "AND (p1 LIKE ? OR p2 LIKE ? OR p3 LIKE ? OR p4 LIKE ? OR p5 LIKE ? "
                          "OR p6 LIKE ? OR p7 LIKE ? OR p8 LIKE ? OR p9 LIKE ? OR p10 LIKE ? "
                          "OR p11 LIKE ? OR p12 LIKE ? OR p13 LIKE ? OR p14 LIKE ? OR p15 LIKE ? "
                          "OR p16 LIKE ? OR p17 LIKE ? OR p18 LIKE ? OR p19 LIKE ? OR p20 LIKE ?)")
            query.addBindValue(da_st)
            query.addBindValue(da_du)
            query.addBindValue(edp2)
            query.addBindValue(edp2)
            query.addBindValue(edp2)
            query.addBindValue(edp2)
            query.addBindValue(edp2)
            query.addBindValue(edp2)
            query.addBindValue(edp2)
            query.addBindValue(edp2)
            query.addBindValue(edp2)
            query.addBindValue(edp2)
            query.addBindValue(edp2)
            query.addBindValue(edp2)
            query.addBindValue(edp2)
            query.addBindValue(edp2)
            query.addBindValue(edp2)
            query.addBindValue(edp2)
            query.addBindValue(edp2)
            query.addBindValue(edp2)
            query.addBindValue(edp2)
            query.addBindValue(edp2)
            query.exec()
            while query.next():
                self.sell_out_results.append(query.value(0))
                self.sell_out_results.append(query.value(1))
                self.sell_out_results.append(query.value(2))
                self.sell_out_results.append(query.value(3))
                self.sell_out_results.append(query.value(4))
                self.sell_out_results.append(query.value(5))
            print("Search_sellout")
            self.conn.commit()
            return self.sell_out_results

    def sell_outlistsearch(self, inv):
        self.list_results = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT * FROM invoice WHERE iv = ?")
            query.addBindValue(inv)
            query.exec()
            while query.next():
                for n in range(96):
                    self.list_results.append(str(query.value(n)))
            self.conn.commit()
            return self.list_results


    ### balance_stock ###

    def balance_group(self):
        try:
            print("------------------")
            self.pdn,self.pdnu = self.blance_stock_name()
            print(self.pdn)
            print(self.pdnu)
            print("------------------")
            #self.test = "Solove F5 Portable Fan-Black"
            for index in range(self.pdnu):
                print("------product-inv-begin-----------")
                self.invname,self.invnu = self.balance_stock_inv(self.pdn[index])
                #print(self.invname)
                #print(self.invnu)
                self.toinvqty = self.total_blance_invqty(self.invname,self.invnu)
                #print(self.toinvqty)
                print("------product-inv-end-----------")
                print("------product-pur-begin-----------")
                self.purname,self.purnu = self.balance_stock_pur(self.pdn[index])
                #print(self.purname)
                #print(self.purnu)
                self.topurqty = self.total_blance_purqty(self.purname,self.purnu)
                #print(self.topurqty)
                print("------product-pur-end-----------")
                print("------product-ret-begin-----------")
                self.retname,self.retnu = self.balance_stock_ret(self.pdn[index])
                #print(self.retname)
                #print(self.retnu)
                self.toretqty = self.total_blance_retqty(self.retname,self.retnu)
                #print(self.toretqty)
                print("------product-ret-end-----------")
                print("------product-renew_stock-begin-----------")
                self.renew_stock = self.topurqty - self.toinvqty + self.toretqty
                print("Stock Balance : " + str(self.renew_stock))
                print("------product-renew_stock-end-----------")
                print("------upload_stock-begin-----------")
                self.upload_balance_stock(self.pdn[index],self.renew_stock)
                print("------upload_stock-end-----------")
            print("------------------")
        except IOError:
            QMessageBox.about(self, "About", "Error !", )
        else:
            pass

    def upload_balance_stock(self,name,stock):
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("UPDATE lib SET stock=? WHERE name=? ")
            query.addBindValue(stock)
            query.addBindValue(name)
            query.exec()
            print("Upload balance_stock db")
            self.conn.commit()


    def blance_stock_name(self):
        self.name = []
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.exec_("SELECT name FROM lib")
            while query.next():
                self.name.append(query.value(0))
            return self.name,len(self.name)


    def balance_stock_inv(self,name):
        self.balance = []
        self.edp2 = name 
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT iv FROM invoice WHERE  \
                          p1 = ? OR p2 = ? OR p3 = ? OR p4 = ? OR p5 = ? \
                          OR p6 = ? OR p7 = ? OR p8 = ? OR p9 = ? OR p10 = ? \
                          OR p11 = ? OR p12 = ? OR p13 = ? OR p14 = ? OR p15 = ? \
                          OR p16 = ? OR p17 = ? OR p18 = ? OR p19 = ? OR p20 = ?")
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.exec()
            while query.next():
                self.balance.append(query.value(0))
            #print("Search_balance")
            #print(self.name + self.balance)
            self.conn.commit()
            return self.edp2,self.balance
    
    def balance_inv_qty(self,name,inv):
        if self.conn.open():
            self.balance_qty = []
            for step in range(1,21):
                self.word = ("SELECT p","p FROM invoice WHERE iv = ? AND p","= ?");
                self.sql= str(step).join(self.word);
                query = QSqlQuery(self.conn)
                query.prepare(self.sql)
                query.addBindValue(inv)
                query.addBindValue(name)
                query.exec()
                while query.next():
                    self.balance_qty.append(query.value(0))
                #print("Search_balance_inv_qty")
                #print(inv)
                #print(self.balance_qty)
                self.conn.commit()
            return sum(self.balance_qty)

    def total_blance_invqty(self,name,inv):
        self.to_balance_sumqty = []
        print(name)
        print(inv)
        for step in range(len(inv)):
            self.to_balance_qty = self.balance_inv_qty(name,inv[step])
            self.to_balance_sumqty.append(self.to_balance_qty)
        print(self.to_balance_sumqty)
        print(sum(self.to_balance_sumqty))
        return sum(self.to_balance_sumqty)


    def balance_stock_pur(self,name):
        self.balance = []
        self.edp2 = name
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT number_no FROM purchase WHERE \
                          p1_name = ? OR p2_name = ? OR p3_name = ? OR p4_name = ? OR p5_name = ? \
                          OR p6_name = ? OR p7_name = ? OR p8_name = ? OR p9_name = ? OR p10_name = ? \
                          OR p11_name = ? OR p12_name = ? OR p13_name = ? OR p14_name = ? OR p15_name = ? \
                          OR p16_name = ? OR p17_name = ? OR p18_name = ? OR p19_name = ? OR p20_name = ?")
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.exec()
            while query.next():
                self.balance.append(query.value(0))
            #print("Search_balance_pur")
            #print(self.balance)
            self.conn.commit()
            return self.edp2,self.balance

    def balance_pur_qty(self,name,inv):
        if self.conn.open():
            self.balance_qty = []
            for step in range(1,21):
                self.word = ("SELECT p","_qty FROM purchase WHERE number_no = ? AND p","_name= ?");
                self.sql= str(step).join(self.word);
                query = QSqlQuery(self.conn)
                query.prepare(self.sql)
                query.addBindValue(inv)
                query.addBindValue(name)
                query.exec()
                while query.next():
                    self.balance_qty.append(query.value(0))
                #print("Search_balance_pur_qty")
                #print(inv)
                #print(self.balance_qty)
                self.conn.commit()
            return sum(self.balance_qty)

    def total_blance_purqty(self,name,inv):
        self.to_balance_sumqty = []
        print(name)
        print(inv)
        for step in range(len(inv)):
            self.to_balance_qty = self.balance_pur_qty(name,inv[step])
            self.to_balance_sumqty.append(self.to_balance_qty)
        print(self.to_balance_sumqty)
        print(sum(self.to_balance_sumqty))
        return sum(self.to_balance_sumqty)

    def balance_stock_ret(self,name):
        self.balance = []
        self.edp2 =  name 
        if self.conn.open():
            query = QSqlQuery(self.conn)
            query.prepare("SELECT iv FROM return WHERE  \
                          p1 = ? OR p2 = ? OR p3 = ? OR p4 = ? OR p5 = ? \
                          OR p6 = ? OR p7 = ? OR p8 = ? OR p9 = ? OR p10 = ? \
                          OR p11 = ? OR p12 = ? OR p13 = ? OR p14 = ? OR p15 = ? \
                          OR p16 = ? OR p17 = ? OR p18 = ? OR p19 = ? OR p20 = ?")
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.addBindValue(self.edp2)
            query.exec()
            while query.next():
                self.balance.append(query.value(0))
            #print("Search_balance_ret")
            #print(self.balance)
            self.conn.commit()
            return self.edp2,self.balance

    def balance_ret_qty(self,name,inv):
        if self.conn.open():
            self.balance_qty = []
            for step in range(1,21):
                self.word = ("SELECT p","p FROM return WHERE iv = ? AND p","= ?");
                self.sql= str(step).join(self.word);
                query = QSqlQuery(self.conn)
                query.prepare(self.sql)
                query.addBindValue(inv)
                query.addBindValue(name)
                query.exec()
                while query.next():
                    self.balance_qty.append(query.value(0))
                #print("Search_balance_pur_qty")
                #print(inv)
                #print(self.balance_qty)
                self.conn.commit()
            return sum(self.balance_qty)

    def total_blance_retqty(self,name,inv):
        self.to_balance_sumqty = []
        print(name)
        print(inv)
        for step in range(len(inv)):
            self.to_balance_qty = self.balance_ret_qty(name,inv[step])
            self.to_balance_sumqty.append(self.to_balance_qty)
        print(self.to_balance_sumqty)
        print(sum(self.to_balance_sumqty))
        return sum(self.to_balance_sumqty)

    ### balance_stock ###

    def closedb(self):
        self.conn.close()
        print("Close")

    def commitdb(self):
        self.conn.commit()
        print("Commit")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    database()
    sys.exit(app.exec_())
