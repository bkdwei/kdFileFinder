#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Created on 2019年3月7日

@author: bkd
'''

from os.path import join,dirname,isdir,isfile
import sys
import subprocess
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot,QDir,Qt
from PyQt5.QtWidgets import  QMainWindow,QApplication,QComboBox,QFileSystemModel
from .fileutil import get_file_realpath

class kdFileFinder(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(get_file_realpath("kdFileFinder.ui"), self)
        self.lw_main.clicked.connect(self.on_lw_main_clicked)
        self.lw_main.doubleClicked.connect(self.on_lw_main_dbclicked)
        self.lw_main.installEventFilter(self)
        self.fileSystemModel.setReadOnly(True)
        self.fileSystemModel = QFileSystemModel(self.lw_main)
        root = self.fileSystemModel.setRootPath("/tmp")
        self.lw_main.setModel(self.fileSystemModel)
        self.lw_main.setRootIndex(root)

        self.le_path.returnPressed.connect(self.on_pb_load_path_clicked)
        
        #TODO for test
        self.qdir = QDir()
        comboBox1 = QComboBox()
        comboBox1.addItem("/tmp")
        comboBox1.addItem("/etc")
        self.hl_bookmark.addWidget(comboBox1)
        comboBox2 = QComboBox()
        comboBox2.addItem("/usr")
        comboBox2.addItem("/home/bkd")
        self.hl_bookmark.addWidget(comboBox2)

    @pyqtSlot()
    def on_pb_load_path_clicked(self):
        root = self.fileSystemModel.setRootPath(self.le_path.text())
        self.lw_main.setRootIndex(root)
    
    def eventFilter(self, qobject, qevent):
        qtype = qevent.type()
#         print("qtype",qtype)
#         print("qobject",qobject)
        if qtype == 82 :
            i = self.lw_main.indexAt(qevent.pos())
            
            if i.isValid() :
                print("鼠标在:" ,i.isValid())
            else:
                paren_dir = dirname(self.le_path.text()) 
                print("单击了右键" + paren_dir)
                self.le_path.setText(paren_dir)
                self.on_pb_load_path_clicked()
        elif qtype == 6 :
                curKey = qevent.key()
                print("按下：" + str(qevent.key()))
                if curKey == Qt.Key_M :
                    self.last_open_dir.append(self.le_path)
                    print(self.last_open_dir)
        return False
    
    @pyqtSlot()
    def on_lw_main_clicked(self):
        cur_item_index = self.lw_main.currentIndex()
        cur_item1 = self.fileSystemModel.itemData(cur_item_index)
        cur_item = cur_item1[0]
        print("cur_item",cur_item1)
        sub_path = join(self.le_path.text(),cur_item)
        print("sub_path:" + sub_path)
        if isdir(str(sub_path)) :
            print(sub_path + "is a dir")
            self.le_path.setText(sub_path)
            self.on_pb_load_path_clicked()
        elif isfile(str(sub_path)):
            print(sub_path + " is a file")
        else:
            print(type(sub_path))
    @pyqtSlot()
    def on_lw_main_dbclicked(self):
        cur_item_index = self.lw_main.currentIndex()
        cur_item1 = self.fileSystemModel.itemData(cur_item_index)
        cur_item = cur_item1[0]
        sub_path = join(self.le_path.text(),cur_item)
        print("hihidb" + sub_path)
        if isfile(sub_path) :
            self.last_open_file.append(sub_path)
            subprocess.call(["xdg-open", sub_path])
    
    def keyPressEvent(self, event):
        curKey = event.key()
        print("按下：" + str(event.key()))
        if curKey == Qt.Key_M:
            self.last_open_dir.append(self.le_path)
            print(self.last_open_dir)
        return False
def main():
    app = QApplication(sys.argv)
    win = kdFileFinder()
    win.showMaximized()
    sys.exit(app.exec_())