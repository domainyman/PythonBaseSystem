# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QMessageBox
from detectstock import Ui_stockdetect
from connectdb import database


class Calldetectst(QMainWindow, Ui_stockdetect):

    def __init__(self, parent=None):
        super(Calldetectst, self).__init__(parent)
        self.setupUi(self)
        self.condb = database()
        self.bu_click()
        

    def tesk(self):
        try:
            reply = QMessageBox.information(self, "Detect Stock", "Detect Stock ? ",
            QMessageBox.Yes | QMessageBox.Close, QMessageBox.Close)
            if reply == QMessageBox.Yes:
                self.condb.balance_group()
                QMessageBox.about(self, "About", "Done. !", )
                self.close()
        except IOError:
            QMessageBox.about(self, "About", "Error !", )
        else:
            pass

    def bu_click(self):
        self.check.clicked.connect(self.tesk)

    def closeEvent(self, event):
        self.condb.closedb()
        print('window close')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Calldetectst()
    win.show()
    sys.exit(app.exec_())
