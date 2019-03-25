'''
Created on 2019年3月25日

@author: bkd
'''
from PyQt5.QtWidgets import  QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from .fileutil import get_file_realpath
from .customer_script import customer_script
class script_manager(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(get_file_realpath("script_manager.ui"), self)
        self.customer_script = customer_script()
    @pyqtSlot()
    def on_pb_add_script_clicked(self):
        self.customer_script.exec_()