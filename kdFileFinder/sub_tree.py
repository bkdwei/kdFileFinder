'''
Created on 2019年3月7日

@author: bkd
'''
 # -*- coding:utf-8 -*-

import os
import sys
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot,QEvent
from PyQt5.QtWidgets import QWidget, QDialog, QMainWindow,QApplication,QDesktopWidget,QListWidgetItem
import time

class sub_tree(QWidget):
    def __init__(self,parent_path,parent_widget):
        super().__init__()
        self.parent_path = parent_path
        self.parent_widget =parent_widget
        loadUi("sub_tree.ui", self)
        self.win_height = QDesktopWidget().geometry().height()
        self.selected = 0
        self.selected_item= None
        self.lw_sub_tree.installEventFilter(self)
#         parent_widget.raise_()

#     @pyqtSlot()
    def on_lw_sub_tree_clicked(self):
#         time.sleep(3)
#         if not self.underMouse() :
#             return 
        cur_item =os.path.join(self.parent_path,self.lw_sub_tree.currentItem().text())
        print(cur_item)
        files = os.listdir(cur_item)
        print(os.listdir(cur_item))
        self.sub = sub_tree(cur_item,self)
        #         for f in files:
#         for f in files:
#             q = QListWidgetItem(f)
#             q.itemEntered.connect(self.sayHi())
        self.sub.lw_sub_tree.addItems(files)
#         for item in self.sub.lw_sub_tree.i
        self.sub.show()
        print(self.frameGeometry())
        pos = self.frameGeometry()
        self.sub.move(pos.x() + pos.width(),(self.win_height - pos.height())/2)
#         self.lw_sub_tree.setFocus()
        self.parent_path.show()
        self.parent_path.exec_()

    def eventFilter(self, qobject, qevent):
        qtype = qevent.type()
        print("qtype",qtype)
        if qtype == 110:
            print("enter")
            i = self.lw_sub_tree.itemAt(qevent.pos())
            print("鼠标在:" + i.text())
            self.lw_sub_tree.setCurrentItem(i)
            self.on_lw_sub_tree_clicked()
            return False
#             if self.selected == 0:
#                 self.selected = 1
#                 i = self.lw_sub_tree.itemAt(qevent.pos())
#                 print("鼠标在:" + i.text())
#                 self.lw_sub_tree.setCurrentItem(i)
#                 self.selected_item = self.lw_sub_tree.currentItem()
#             elif self.selected == 1:
#                 time.sleep(1)
#                 self.selected = 2
#                 self.lw_sub_tree.setCurrentItem(self.lw_sub_tree.itemAt(qevent.pos()))
#             elif self.selected == 2 and self.selected_item == self.lw_sub_tree.currentItem():
#                 self.lw_sub_tree.setCurrentItem(self.lw_sub_tree.itemAt(qevent.pos()))
#                 print("open "+self.lw_sub_tree.currentItem().text())
# #                 self.on_lw_sub_tree_clicked()
#                 return False
#             else :
#                 self.selected = 0
#                 self.selected_item = None
#         elif qtype ==  10:
#             print("leave")
#             self.selected = 0
        return False
    def moveCursor(self):
        print("sender")
    def sayHi(self):
        print("hi")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = sub_tree()
    win.show()
    sys.exit(app.exec_())