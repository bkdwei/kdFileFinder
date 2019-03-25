'''
Created on 2019年3月25日

@author: bkd
'''
from PyQt5.QtWidgets import  QDialog
from PyQt5.uic import loadUi
from .fileutil import get_file_realpath
class customer_script(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(get_file_realpath("customer_script.ui"), self)

    