'''
Created on 2019年3月7日

@author: bkd
'''
 # -*- coding:utf-8 -*-

import os
from os.path import join,dirname,isdir,isfile
import sys
import subprocess
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot,QDir,QFile,QSize,Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import  QMainWindow,QApplication,QDesktopWidget,QListWidgetItem,QComboBox,QStyleOptionViewItem,QStyledItemDelegate,QFileSystemModel
from .fileutil import get_file_realpath

class ItemDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        option.decorationPosition = QStyleOptionViewItem.Right
        super(ItemDelegate, self).paint(painter, option, index)
        
class kdFileFinder(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(get_file_realpath("kdFileFinder.ui"), self)
        self.lw1.next_lw = self.lw2
        self.lw2.next_lw = self.lw3
        self.lw3.next_lw = self.lw1
        self.lw1.clicked.connect(lambda: self.on_lw_clicked(self.lw1))
        self.lw2.clicked.connect(lambda: self.on_lw_clicked(self.lw2))
        self.lw3.clicked.connect(lambda: self.on_lw_clicked(self.lw3))
        self.qdir = QDir()
        self.cur_lw = self.lw1
        self.global_path = "/"
        self.lw_main.clicked.connect(self.on_lw_main_clicked)
        self.lw_main.doubleClicked.connect(self.on_lw_main_dbclicked)
        self.lw_main.installEventFilter(self)
#         self.lw_main.keyPressed.connect(self.keyPressEvent)
        self.le_path.returnPressed.connect(self.on_pb_load_path_clicked)
        comboBox1 = QComboBox()
        comboBox1.addItem("/tmp")
        comboBox1.addItem("/etc")
        self.hl_bookmark.addWidget(comboBox1)
        comboBox2 = QComboBox()
        comboBox2.addItem("/usr")
        comboBox2.addItem("/home/bkd")
        self.hl_bookmark.addWidget(comboBox2)
        
        self.last_open_file =[]
        self.last_open_dir = []
        
        self.dir_icon = QIcon(get_file_realpath("21.png"))
        self.delegate = ItemDelegate()
#         self.lw_main.setItemDelegate(self.delegate)
#         self.lw_main.setItemAlignment(Qt.AlignLeft)
#         self.lw_main.setStyleSheet("QListWidget{min-width: 100px; border:none; border-top:2px solid #4da8e8; color:#ffffff; margin: 0 0 0 0; padding: 0 0 0 0; text-align:center;} QListWidget::item{border-bottom: 2px solid #4da8e8; padding:15px 25px 15px 25px; margin: 0 0 0 0; text-align: center; background:#399ee5; color:#ffffff;} QListWidget::item:hover{border:none; background:#45c8dc; font-weight:bold;} QListWidget::item:selected{border:none; border-left: 6px solid #fa7064; background:#ffffff; color:#fa7064; font-weight:bold;} QListWidget::icon{margin: 0 0 0 0; padding: 0 20px 0 0;} QLabel{background:transparent; border: none; font-size: 15pt; color:#ffffff; font-family:'Segoe UI';}")

        self.fileSystemModel = QFileSystemModel(self.lw_main)
        self.fileSystemModel.setReadOnly(True)
        self.lw_main.setModel(self.fileSystemModel)
        root = self.fileSystemModel.setRootPath("/tmp")
        self.lw_main.setRootIndex(root)

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
        for i in files:
            v = QListWidgetItem(i)
            v.setStylesheet("*:hover {background:gray;}")
            self.lw1.addItem(v)
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
        
    @pyqtSlot()
    def on_pb_load_path_clicked(self):
#         self.lw_main.setIconSize(QSize(20, 20)); 
#         self.lw_main.setGridSize(QSize(200, 20)); 
#         cur_dir = self.le_path.text()
#         self.qdir.setPath(cur_dir)
#         files = self.qdir.entryList()
#         for f in files:
#             if f.startswith(".") :
#                 files.remove(f)
#         self.lw_main.clear()
#         files.sort()
#         for file in files:
#             if isdir(join(cur_dir,file)):
#                 print(file + " is a dir")
#                 list_item = QListWidgetItem(file)
#                 list_item.setIcon(self.dir_icon)
#                 list_item.setTextAlignment(Qt.AlignVCenter)
#                 self.lw_main.addItem(list_item)
#             else :
#                 self.lw_main.addItem(file)
        print(self.le_path.text())
        root = self.fileSystemModel.setRootPath(self.le_path.text())
        self.lw_main.setRootIndex(root)
        print("bkd")
                
    
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
        if os.path.isdir(str(sub_path)) :
            print(sub_path + "is a dir")
            self.le_path.setText(sub_path)
            self.on_pb_load_path_clicked()
        elif os.path.isfile(str(sub_path)):
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