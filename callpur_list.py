# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from pur_listui import Ui_ui_pur_list
from connectdb import database
from PyQt5.QtCore import Qt

class callpur_list(QMainWindow, Ui_ui_pur_list):
    my_Signal = QtCore.pyqtSignal()

    def __init__(self, list_info, parent=None):
        super(callpur_list, self).__init__(parent)
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
        self.n1_coed.setText(self.data_info[5])
        self.n1_qtyed.setText(self.data_info[6])
        self.n2.setText(self.data_info[7])
        self.n2_coed.setText(self.data_info[8])
        self.n2_qtyed.setText(self.data_info[9])
        self.n3.setText(self.data_info[10])
        self.n3_coed.setText(self.data_info[11])
        self.n3_qtyed.setText(self.data_info[12])
        self.n4.setText(self.data_info[13])
        self.n4_coed.setText(self.data_info[14])
        self.n4_qtyed.setText(self.data_info[15])
        self.n5.setText(self.data_info[16])
        self.n5_coed.setText(self.data_info[17])
        self.n5_qtyed.setText(self.data_info[18])
        self.n6.setText(self.data_info[19])
        self.n6_coed.setText(self.data_info[20])
        self.n6_qtyed.setText(self.data_info[21])
        self.n7.setText(self.data_info[22])
        self.n7_coed.setText(self.data_info[23])
        self.n7_qtyed.setText(self.data_info[24])
        self.n8.setText(self.data_info[25])
        self.n8_coed.setText(self.data_info[26])
        self.n8_qtyed.setText(self.data_info[27])
        self.n9.setText(self.data_info[28])
        self.n9_coed.setText(self.data_info[29])
        self.n9_qtyed.setText(self.data_info[30])
        self.n10.setText(self.data_info[31])
        self.n10_coed.setText(self.data_info[32])
        self.n10_qtyed.setText(self.data_info[33])
        self.n11.setText(self.data_info[34])
        self.n11_coed.setText(self.data_info[35])
        self.n11_qtyed.setText(self.data_info[36])
        self.n12.setText(self.data_info[37])
        self.n12_coed.setText(self.data_info[38])
        self.n12_qtyed.setText(self.data_info[39])
        self.n13.setText(self.data_info[40])
        self.n13_coed.setText(self.data_info[41])
        self.n13_qtyed.setText(self.data_info[42])
        self.n14.setText(self.data_info[43])
        self.n14_coed.setText(self.data_info[44])
        self.n14_qtyed.setText(self.data_info[45])
        self.n15.setText(self.data_info[46])
        self.n15_coed.setText(self.data_info[47])
        self.n15_qtyed.setText(self.data_info[48])
        self.n16.setText(self.data_info[49])
        self.n16_coed.setText(self.data_info[50])
        self.n16_qtyed.setText(self.data_info[51])
        self.n17.setText(self.data_info[52])
        self.n17_coed.setText(self.data_info[53])
        self.n17_qtyed.setText(self.data_info[54])
        self.n18.setText(self.data_info[55])
        self.n18_coed.setText(self.data_info[56])
        self.n18_qtyed.setText(self.data_info[57])
        self.n19.setText(self.data_info[58])
        self.n19_coed.setText(self.data_info[59])
        self.n19_qtyed.setText(self.data_info[60])
        self.n20.setText(self.data_info[61])
        self.n20_coed.setText(self.data_info[62])
        self.n20_qtyed.setText(self.data_info[63])
        self.am_ed.setText(self.data_info[64])
        self.qty_ed.setText(self.data_info[65])

    def del_pur_bu(self):
        reply = QMessageBox.information(self, "Delete No.", "Once deleted , Invoice cannot be recovered!",
                                        QMessageBox.Yes | QMessageBox.Close, QMessageBox.Close)
        if reply == QMessageBox.Yes:
            self.iv = self.data_inv
            print(self.iv)
            self.purdata = self.condb.select_pur(self.iv)
            self.firdata = self.purdata[4:64]
            self.reindata = [i for i in self.firdata if i != '']
            print(self.reindata)
            self.exc_res = self.condb.excision_results(self.reindata,3)           
            self.condb.delpur_stock(self.exc_res) 
            self.condb.del_purdb(self.iv)
            self.close()


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
            self.condb.up_pur_data(da,inv)
            self.close()

    def sendEditContent(self):
        self.my_Signal.emit()

    def closeEvent(self, event):
        self.sendEditContent()
        self.condb.closedb()
        print('window close')

    def bu_click(self):
        self.del_bu.clicked.connect(self.del_pur_bu)
        self.data_checkBox.stateChanged.connect(self.checkBoxChangedAction)
        self.data_upload.clicked.connect(self.da_up_bu)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = callpur_list()
    win.show()
    sys.exit(app.exec_())
