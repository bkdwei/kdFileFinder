#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Created on 2019年3月7日

@author: bkd
'''

import sys
import subprocess
from os.path import join,dirname,isdir,isfile, basename
from os import system
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot,QDir,Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import  QMainWindow,QApplication,QFileSystemModel,QAction,QListWidgetItem
from .fileutil import get_file_realpath
from . import kdconfig
from . import bookmark

class kdFileFinder(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(get_file_realpath("kdFileFinder.ui"), self)
        self.setWindowIcon(QIcon(get_file_realpath('data/kdFileFinder.png')))
        self.lw_main.clicked.connect(self.on_lw_main_clicked)
        self.lw_main.doubleClicked.connect(self.on_lw_main_dbclicked)
        self.lw_main.installEventFilter(self)
        self.fileSystemModel = QFileSystemModel(self.lw_main)
        self.fileSystemModel.setReadOnly(True)
        self.fileFilter =self.fileSystemModel.filter()
        self.fileFilter_hidden = None
        root = self.fileSystemModel.setRootPath(QDir.home().absolutePath())
        self.lw_main.setModel(self.fileSystemModel)
        self.lw_main.setRootIndex(root)
        self.lw_main.setWrapping(True)

        self.le_path.returnPressed.connect(self.on_pb_load_path_clicked)
        
        self.init_toolbar()
        self.bookmark_list = bookmark.get_bookmark()
        self.init_bookmark()
        self.session_list = set()
        self.last_open_file = set()
    def init_bookmark(self):
        self.lw_sidebar.clear()
        if self.bookmark_list:
            for b in self.bookmark_list:
                self.add_bookmark_or_session(b)
        self.lw_sidebar.currentItemChanged.connect(self.on_lw_sidebar_clicked)
    
    def init_session(self):
        print(self.session_list)
        self.lw_sidebar.clear()
        if self.session_list:
            for b in self.session_list:
                self.add_bookmark_or_session(b)
        self.lw_sidebar.currentItemChanged.connect(self.on_lw_sidebar_clicked)
        
    def init_toolbar(self):
        self.toolBar.addAction(QIcon(get_file_realpath("data/list-add.png")),"新增")
        self.toolBar.addAction(QIcon(get_file_realpath("data/list-remove.png")),"删除")
        self.toolBar.addAction(QIcon(get_file_realpath("data/go-home.png")),"主页")
        self.toolBar.addAction(QIcon(get_file_realpath("data/bookmark-book.png")),"收藏夹")
        self.toolBar.addAction(QIcon(get_file_realpath("data/edit-copy.png")),"标签")
        self.toolBar.addAction(QIcon(get_file_realpath("data/folder.png")),"显示文件夹").setCheckable(True)
        self.toolBar.addAction(QIcon(get_file_realpath("data/eye.png")),"显示隐藏文件").setCheckable(True)
        self.toolBar.addAction(QIcon(get_file_realpath("data/terminal.png")),"终端")
        self.toolBar.addAction(QIcon(get_file_realpath("data/view-list-tree.png")),"我的电脑")
        self.toolBar.addAction(QIcon(get_file_realpath("data/go-up.png")),"返回上层")
        self.toolBar.actionTriggered[QAction].connect(self.on_toolBar_clicked)

    def add_bookmark_or_session(self,path):
            item = QListWidgetItem(basename(path))
            item.setData(-1,path)
            self.lw_sidebar.addItem(item)
    def go_home(self):
        list1 = QDir.drives()
        for l in list1:
            print(l.absolutePath())
        
        self.le_path.setText(QDir.home().absolutePath())
        self.on_pb_load_path_clicked()
        
    def on_toolBar_clicked(self,action):
        action_text = action.text()
        if action_text == "收藏夹" :
            self.lb_sidebar.setText(action_text)
            self.init_bookmark()
        elif action_text == "标签" :
            self.lb_sidebar.setText(action_text)
            self.init_session()
        elif action_text == "主页" :
            self.go_home()
        elif action_text == "终端" :
            system('x-terminal-emulator --working-directory={} &'.format(self.le_path.text()))
        elif action_text == "我的电脑" :
            system('xdg-open ' + self.le_path.text())
        elif action_text == "返回上层" :
            paren_dir = dirname(self.le_path.text()) 
            self.le_path.setText(paren_dir)
            self.on_pb_load_path_clicked()
        elif action_text == "显示隐藏文件" :
            if action.isChecked():
                self.fileFilter_hidden = QDir.Hidden
                self.fileSystemModel.setFilter(self.fileFilter|QDir.Hidden)
            else :
                self.fileFilter_hidden = None
                self.fileSystemModel.setFilter(self.fileFilter)
        elif action_text == "显示文件夹" :
            if action.isChecked():
                if self.fileFilter_hidden :
                    self.fileSystemModel.setFilter(QDir.Dirs|QDir.Hidden|QDir.NoDot|QDir.NoDotDot)
                else:
                    self.fileSystemModel.setFilter(QDir.Dirs|QDir.NoDot|QDir.NoDotDot)
            else :
                self.fileSystemModel.setFilter(self.fileFilter)
        elif action_text == "新增" :
            if self.lb_sidebar.text() == "收藏夹" :
                self.add_bookmark_or_session(self.le_path.text())
                kdconfig.list_add("global", "bookmark", self.le_path.text())
            elif self.lb_sidebar.text() == "标签" :
                self.session_list.add(self.le_path.text())
                self.add_bookmark_or_session(self.le_path.text())
                print(self.session_list)
        elif action_text == "删除" :
            if self.lb_sidebar.text() == "收藏夹" :
                print(self.lw_sidebar.currentRow())
                kdconfig.list_del("global", "bookmark", self.le_path.text())
                self.bookmark_list.discard(self.le_path.text())
                self.lw_sidebar.takeItem(self.lw_sidebar.currentRow())
                print(self.bookmark_list)
            elif self.lb_sidebar.text() == "标签" :
                self.session_list.remove(self.le_path.text())

    @pyqtSlot()
    def on_lw_sidebar_clicked(self):
        cur_item = self.lw_sidebar.currentItem()
        if cur_item :
            cur_item_data = cur_item.data(-1)
            self.le_path.setText(cur_item_data)
            self.on_pb_load_path_clicked()
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
            self.last_open_file.add(sub_path)
            subprocess.call(["xdg-open", sub_path])
            self.showMinimized()
    
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
#     win.showMaximized()
    win.show()
    sys.exit(app.exec_())