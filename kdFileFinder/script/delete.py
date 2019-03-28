'''
Created on 2019年3月26日

@author: bkd
'''
from os import remove
from shutil import rmtree
from os.path import isfile,isdir
class delete:
    def execute(self,script_variable):
        file_path = script_variable["cur_item"]
        if isfile(file_path) :
            remove(file_path)
            print("删除文件成功，" + file_path)
        elif isdir(file_path) :
            rmtree(file_path)
            print("删除目录成功，" + file_path)
        else :
            print("无法删除的项目")    