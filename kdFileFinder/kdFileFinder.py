'''
Created on 2019年3月7日

@author: bkd
'''
 # -*- coding:utf-8 -*-

import os
from os.path import join,dirname
import sys
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot,QDir,QFile
from PyQt5.QtWidgets import  QMainWindow,QApplication,QDesktopWidget

class kdFileFinder(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("kdFileFinder.ui", self)
        self.lw1.next_lw = self.lw2
        self.lw2.next_lw = self.lw3
        self.lw3.next_lw = self.lw1
        self.lw1.clicked.connect(lambda: self.on_lw_clicked(self.lw1))
        self.lw2.clicked.connect(lambda: self.on_lw_clicked(self.lw2))
        self.lw3.clicked.connect(lambda: self.on_lw_clicked(self.lw3))
        self.qdir = QDir()
        self.cur_lw = self.lw1
        self.global_path = "/"

    @pyqtSlot()
    def on_pb_root_clicked(self):
        self.qdir.setPath("/")
        files = self.qdir.entryList()
        self.lw1.parent_path = "/"
        for f in files:
            if f.startswith(".") :
                files.remove(f)
        self.lw1.clear()
        files.sort()
        self.lw1.addItems(files)
    
    @pyqtSlot()
    def on_pb_home_clicked(self):
        self.qdir.setPath("/home")
        files = os.listdir("/home")
        for f in files:
            if f.startswith(".") :
                files.remove(f)
        self.lw1.clear()
        self.lw1.addItems(files)
    @pyqtSlot()
    def on_pb_tmp_clicked(self):
        files = os.listdir("/tmp")
        for f in files:
            if f.startswith(".") :
                del files[f]
        self.lw1.clear()
        self.lw1.addItems(files)
        
    def on_lw_clicked(self,cur_lw):
#         点击自己
        if cur_lw == self.cur_lw :
            self.show_sub_dir(cur_lw)
#         下一个节点被点击
        elif cur_lw == self.cur_lw.next_lw :
            self.show_sub_dir(cur_lw)
#         上一个节点被单击
            self.cur_lw = cur_lw
        else :
            self.show_parent_dir(cur_lw)
            self.show_sub_dir(cur_lw)
            self.cur_lw = cur_lw
        
    def show_parent_dir(self,cur_lw):
        print(cur_lw.objectName())
        parent_dir = dirname(cur_lw.parent_path)
        print(parent_dir)
        self.qdir.setPath(parent_dir)
        files = self.qdir.entryList()
        for f in files:
            if f.startswith(".") :
                files.remove(f)
        parent_lw = cur_lw.next_lw.next_lw
        print(parent_lw.objectName())
        parent_lw.parent_path = parent_dir
        parent_lw.clear()
        files.sort()
        parent_lw.addItems(files)
        
    def show_sub_dir(self,cur_lw):
        cur_dir = join(cur_lw.parent_path,cur_lw.currentItem().text())
        print(cur_dir)
        self.qdir.setPath(cur_dir)
        files = self.qdir.entryList()
        for f in files:
            if f.startswith(".") :
                files.remove(f)
        cur_lw.next_lw.clear()
        cur_lw.next_lw.parent_path = cur_dir
        files.sort()
        cur_lw.next_lw.addItems(files)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = kdFileFinder()
    win.show()
    sys.exit(app.exec_())