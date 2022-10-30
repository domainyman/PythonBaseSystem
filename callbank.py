# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from connectdb import database
from bank import Ui_bank


class Callbank(QMainWindow, Ui_bank):
    def __init__(self, parent=None):
        super(Callbank, self).__init__(parent)
        self.setupUi(self)
        self.condb = database()
        self.bankinfo = self.condb.display_bankinfo()
        self.bankinfo_bu_click()
        self.text_set()

    def upload_cominfo(self):
        reply = QMessageBox.information(self, "Upload Info", "Upload Info ? ",
                                        QMessageBox.Yes | QMessageBox.Close, QMessageBox.Close)
        if reply == QMessageBox.Yes:
            na = self.ac_na_ed.text()
            co = self.bank_cod_ed.text()
            ac = self.bank_acc_ed.text()
            self.condb.bank_info(na, co, ac)
            self.condb.commitdb()

    def text_set(self):
        self.ac_na_ed.setText(self.bankinfo[1])
        self.bank_cod_ed.setText(self.bankinfo[2])
        self.bank_acc_ed.setText(self.bankinfo[3])

    def bankinfo_bu_click(self):
        self.pushButton.clicked.connect(self.upload_cominfo)

    def closeEvent(self, event):
        self.condb.closedb()
        print('window close')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Callbank
    win.show()
    sys.exit(app.exec_())
