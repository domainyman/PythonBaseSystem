# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from connectdb import database
from compinfoui import Ui_compDialog


class Callcompinfo(QMainWindow, Ui_compDialog):
    def __init__(self, parent=None):
        super(Callcompinfo, self).__init__(parent)
        self.setupUi(self)
        self.condb = database()
        self.info = self.condb.display_cominfo()
        self.cominfo_bu_click()
        self.text_set()

    def upload_cominfo(self):
        reply = QMessageBox.information(self, "Upload Info", "Upload Info ? ",
                                        QMessageBox.Yes | QMessageBox.Close, QMessageBox.Close)
        if reply == QMessageBox.Yes and len(self.cn_li.text()) != 0 and len(self.ca_li.text()) != 0:
            cn = self.cn_li.text()
            ca = self.ca_li.text()
            self.condb.comp_info(cn, ca)
            self.condb.commitdb()

    def text_set(self):
        self.cn_li.setText(self.info[1])
        self.ca_li.setText(self.info[2])

    def cominfo_bu_click(self):
        self.up_bu.clicked.connect(self.upload_cominfo)

    def closeEvent(self, event):
        self.condb.closedb()
        print('window close')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Callcompinfo
    win.show()
    sys.exit(app.exec_())