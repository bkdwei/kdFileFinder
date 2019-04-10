'''
Created on 2019年3月26日

@author: bkd

复制文件名
'''
from PyQt5.QtWidgets import QApplication

class copy_filename:
    def execute(self,script_variable):
        cur_file = script_variable["file_list"][0]
        clipboard = QApplication.clipboard()
        clipboard.setText(cur_file)
