# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from connectdb import database
from exp_listui import Ui_exp_list
from PyQt5.QtCore import Qt


class callexp_list(QMainWindow, Ui_exp_list):
    my_Signal = QtCore.pyqtSignal()

    def __init__(self, list_info, parent=None):
        super(callexp_list, self).__init__(parent)
        self.data_info = list_info
        self.data_inv = self.data_info[1]
        self.setupUi(self)
        self.condb = database()
        self.showlist()
        self.bu_click()

    def showlist(self):
        self.no_ed.setText(self.data_info[1])
        self.da_ed.setText(self.data_info[2])
        self.sp_ed.setText(self.data_info[3])
        self.n1.setText(self.data_info[4])
        self.n1_pred.setText(self.data_info[5])
        self.n2.setText(self.data_info[6])
        self.n2_pred.setText(self.data_info[7])
        self.n3.setText(self.data_info[8])
        self.n3_pred.setText(self.data_info[9])
        self.n4.setText(self.data_info[10])
        self.n4_pred.setText(self.data_info[11])
        self.n5.setText(self.data_info[12])
        self.n5_pred.setText(self.data_info[13])
        self.n6.setText(self.data_info[14])
        self.n6_pred.setText(self.data_info[15])
        self.n7.setText(self.data_info[16])
        self.n7_pred.setText(self.data_info[17])
        self.n8.setText(self.data_info[18])
        self.n8_pred.setText(self.data_info[19])
        self.n9.setText(self.data_info[20])
        self.n9_pred.setText(self.data_info[21])
        self.n10.setText(self.data_info[22])
        self.n10_pred.setText(self.data_info[23])
        self.item_ed.setText(self.data_info[24])
        self.am_ed.setText(self.data_info[25])

    def del_exp_bu(self):
        reply = QMessageBox.information(self, "Delete No.", "Once deleted , Invoice cannot be recovered!",
                                        QMessageBox.Yes | QMessageBox.Close, QMessageBox.Close)
        if reply == QMessageBox.Yes:
            self.iv = self.data_inv
            self.condb.del_expdb(self.iv)
            self.close()

    def sendEditContent(self):
        self.my_Signal.emit()

    def checkBoxChangedAction(self, state):
        if state == Qt.Checked:
            self.da_ed.setEnabled(True)
        else:
            self.da_ed.setEnabled(False)

    def da_up_bu(self):
        reply = QMessageBox.information(self, "UPLOAD Date", "Once UPLOAD , Invoice cannot be recovered!",
                                        QMessageBox.Yes | QMessageBox.Close, QMessageBox.Close)
        if reply == QMessageBox.Yes:
            inv = self.no_ed.text()
            da = self.da_ed.text()
            self.condb.up_exp_data(da,inv)
            self.close()

    def closeEvent(self, event):
        self.sendEditContent()
        self.condb.closedb()
        print('window close')

    def bu_click(self):
        self.del_bu.clicked.connect(self.del_exp_bu)
        self.data_checkBox.stateChanged.connect(self.checkBoxChangedAction)
        self.data_upload.clicked.connect(self.da_up_bu)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = callexp_list()
    win.show()
    sys.exit(app.exec_())
