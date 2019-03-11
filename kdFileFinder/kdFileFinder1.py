'''
Created on 2019年3月7日

@author: bkd
'''
 # -*- coding:utf-8 -*-

import os
import sys
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import  QMainWindow,QApplication,QDesktopWidget
from sub_tree import  sub_tree
from kdFileFinder import constant

class kdFileFinder(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("kdFileFinder.ui", self)
        self.lw_main.addItem("/")
        self.lw_main.addItem("/home")
        self.win_height = QDesktopWidget().geometry().height()

#     @pyqtSlot()
    def on_lw_main_clicked(self):
        cur_item = self.lw_main.currentItem().text()
        files = os.listdir(cur_item)
        print(os.listdir(cur_item))
        self.sub = sub_tree(cur_item,self)
#         for f in files:
        self.sub.lw_sub_tree.addItems(files)
        self.sub.setVisible(True)
        self.show()
        self.exec_()
        print(self.frameGeometry())
        pos = self.frameGeometry()
        self.sub.move(pos.x() + pos.width(),(self.win_height - pos.height())/2)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = kdFileFinder()
    win.show()
    sys.exit(app.exec_())