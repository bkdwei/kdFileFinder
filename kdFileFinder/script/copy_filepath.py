'''
Created on 2019年3月26日

@author: bkd

复制文件的完整路径
'''
from PyQt5.QtWidgets import QApplication
from os.path import join

class copy_filepath:
    def execute(self,script_variable):
        cur_filepath = join(script_variable["cur_path"],script_variable["file_list"][0])
        clipboard = QApplication.clipboard()
        clipboard.setText(cur_filepath)
