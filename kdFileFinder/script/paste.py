'''
Created on 2019年3月26日

@author: bkd
'''
from shutil import copy2,copytree,rmtree
from os.path import basename,join,exists,isfile,isdir
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QGuiApplication

class paste(QMessageBox):
    def execute(self,script_variable):
        cur_path = script_variable["cur_path"]

        clipboard = QGuiApplication.clipboard()
        mimeData = clipboard.mimeData()
        if not mimeData.hasFormat("text/uri-list") :
            print("剪切板为空")
            return
        
        urls = mimeData.urls()
        for  u in urls:
            src = u.path()
            dst = join(cur_path,basename(src))
            is_exists = exists(dst)
            if isfile(src) :
                self.copy_file(is_exists, src, dst)
            elif isdir(src) :
                self.copy_dir(is_exists, src, dst)
            else :
                print("无法复制的项目")
    def copy_file(self,is_exists,src,dst):
        if is_exists :
            reply = self.information(self, "确认文件替换",   "该位置已存在一个同名的文件" + basename(src), QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                print("目标文件已存在")
                print("复制文件：" + src + "->" + dst)
                copy2(src,dst)
        else :
                print("复制文件：" + src + "->" + dst)
                copy2(src,dst)
    def copy_dir(self,is_exists,src,dst):
        if  is_exists:
                reply = self.information(self, "确认文件夹替换",   "该位置已存在一个同名的文件夹" + basename(src), QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                    print("删除已存在的目标文件夹：" + dst)
                    rmtree(dst)
                    print("复制文件夹：" + src + "->" + dst)
                    copytree(src,dst)
        else :
            print("复制文件夹：" + src + "->" + dst)
            copytree(src,dst)
