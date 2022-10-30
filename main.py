# -*- coding: utf-8 -*-
import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainui import Ui_MainWindow
from callproductedit import Callproductedit
from callpurchase import Callpurchase
from invoice import Callinvoice
from callexpense import callexpense
from callcn import Callcn
from callcheqrec import Callcheqrec
from callreport_stat import Callreport
from callpl_report import Callplreport
from callclient import Callclient
from callbank import Callbank
from callcompinfo import Callcompinfo
from callreturn import Callreturn
from callinv_ed import Callin_ed
from callsell_out_rep import Callsell_out_rep
from calldetectstock import Calldetectst
from PyQt5.QtCore import QCoreApplication 
from PyQt5.QtCore import Qt 
from connectdb import database
from PyQt5.QtCore import pyqtSignal, QThread

class qthread(QThread):
    signal = pyqtSignal(str)
    def __init__(self):
        super(qthread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        pass

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setWindowFlags(Qt.WindowMinMaxButtonsHint)
        self.setWindowModality(Qt.NonModal)
        self.setupUi(self)
        self.main_bu()
        self.condb = database()
        self.condb.balance_group()

    def c_pro(self):
        self._call_pde = Callproductedit()
        self._call_pde.show()

    def c_inv(self):
        self._call_inv = Callinvoice()
        self._call_inv.show()

    def c_pur(self):
        self._call_pur = Callpurchase()
        self._call_pur.show()

    def c_exp(self):
        self._call_exp = callexpense()
        self._call_exp.show()

    def c_cn(self):
        self._call_cn = Callcn()
        self._call_cn.show()

    def c_cheqrec(self):
        self._call_cheqrec = Callcheqrec()
        self._call_cheqrec.show()

    def c_report(self):
        self._call_report = Callreport()
        self._call_report.show()

    def c_plreport(self):
        self._call_plreport = Callplreport()
        self._call_plreport.show()

    def c_client(self):
        self._call_client = Callclient()
        self._call_client.show()

    def c_bank(self):
        self._call_bank = Callbank()
        self._call_bank.show()

    def c_comp(self):
        self._call_comp = Callcompinfo()
        self._call_comp.show()

    def c_ret(self):
        self._call_ret = Callreturn()
        self._call_ret.show()

    def c_selloutrep(self):
        self._call_selloutrep = Callsell_out_rep()
        self._call_selloutrep.show()

    def c_inv_ed(self):
        self._call_inv_ed = Callin_ed()
        self._call_inv_ed.show()

    def c_de_st(self):
        self._call_dectst = Calldetectst()
        self._call_dectst.show()


    def c_copy(self, remaining, total):
        print(f'Copied {total - remaining} of {total} pages...')

    try:
        con = sqlite3.connect('viewmaxdb.db')
        bck = sqlite3.connect('backup.db')
        with bck:
            con.backup(bck, pages=-1, progress=c_copy)
        print("Backup successful")
    except sqlite3.Error as error:
        print("Error while taking backup: ", error)
    finally:
        if bck:
            con.close()
            bck.close()

    def main_bu(self):
        self.product.clicked.connect(self.c_pro)
        self.invoice.clicked.connect(self.c_inv)
        self.purchase.clicked.connect(self.c_pur)
        self.expense.clicked.connect(self.c_exp)
        self.cn.clicked.connect(self.c_cn)
        self.cheq.clicked.connect(self.c_cheqrec)
        self.statement.clicked.connect(self.c_report)
        self.pl.clicked.connect(self.c_plreport)
        self.client.clicked.connect(self.c_client)
        self.bank_info.clicked.connect(self.c_bank)
        self.comp.clicked.connect(self.c_comp)
        self.returnnote.clicked.connect(self.c_ret)
        self.inv_ed.clicked.connect(self.c_inv_ed)
        self.detect_stock.clicked.connect(self.c_de_st)
        self.sell_out_rep.clicked.connect(self.c_selloutrep)
        self.exit.clicked.connect(QCoreApplication.instance().quit)

    def closeEvent(self, event):
        QApplication.closeAllWindows()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())
