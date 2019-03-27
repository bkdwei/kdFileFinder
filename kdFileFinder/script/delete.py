'''
Created on 2019年3月26日

@author: bkd
'''
from os import remove
class delete:
    def execute(self,cur_item,script_variable):
        remove(script_variable["cur_item"])
        print("删除文件成功" + script_variable["cur_item"])