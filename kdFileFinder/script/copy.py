'''
Created on 2019年3月26日

@author: bkd

复制功能，可以和其他程序进行复制粘贴操作
'''
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QMimeData

class copy:
    def execute(self,script_variable):
        cur_path = script_variable["cur_path"]
        file_list = script_variable["file_list"]
        
        files = ""
        for f in file_list :
            files += "file://" +  cur_path + "/" + f + "\r\n"
        
        mimeData = QMimeData()
        mimeData.setData("text/uri-list",files.encode())
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimeData)
        
        print("成功复制到剪切板" , files)