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
        self.rb_cur_item.apply_type = 1
        self.rb_other_filetype.apply_type = 2

    
    def edit(self,script):
        self.le_name.setText(script["name"])
        self.le_path.setText(script["path"])
        self.le_filetype.setText(script["filetype"])
        if script["apply_type"] == 1:
            self.rb_cur_item.setChecked(True)
        else :
            self.rb_other_filetype.setChecked(True)