'''
Created on 2019年3月26日

@author: bkd
'''
from shutil import copy2,copytree,rmtree
from os.path import basename,join,exists
from os.path import isfile,isdir
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QGuiApplication

class paste(QMessageBox):
    def execute(self,script_variable):
        cur_item = script_variable["cur_item"]
        cur_path = script_variable["cur_path"]
#         从其他文件管理利器读取复制的文件
        if 2>1 :
            clipboard = QGuiApplication.clipboard()
            urls = clipboard.mimeData().urls()
            print(type(urls))
            for  x in urls:
                print("从其他文件管理器获得待粘贴文件列表",x.path())
            return
        already_exists = exists(join(cur_path,basename(cur_item)))
        
        if isfile(cur_item) :
            if  already_exists:
                reply = self.information(self, "确认文件替换",   "该位置已存在一个同名的文件", QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                    print("目标文件已存在")
                    copy2(cur_item,cur_path)
                    script_variable["copy_item"] = None
        elif isdir(cur_item) :
            if  already_exists:
                reply = self.information(self, "确认文件夹替换",   "该位置已存在一个同名的文件夹", QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                    print("目标文件夹已存在" + join(cur_path,basename(cur_item)))
                    rmtree(join(cur_path,basename(cur_item)))
                    copytree(cur_item,join(cur_path,basename(cur_item)))
                    script_variable["copy_item"] = None
            else :
                copytree(cur_item,join(cur_path,basename(cur_item)))
                script_variable["copy_item"] = None
        else :
            print("无法复制的项目")    