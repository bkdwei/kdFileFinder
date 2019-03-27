'''
Created on 2019年3月26日

@author: bkd
'''
import shutil
from PyQt5.QtWidgets import QMessageBox
from os.path import basename

class paste:
    def execute(self,script_variable):
        print("复制" + script_variable["copy_item"] + "到" +script_variable["cur_path"])
        shutil.copy2(script_variable["copy_item"],script_variable["cur_path"])
        script_variable["script_result_body"] = "粘贴文件成功，文件：" + basename(script_variable["copy_item"])
#         QMessageBox.information(self,     "粘贴文件",      "粘贴文件成功，文件：" + basename(script_variable["copy_item"]) ) 
