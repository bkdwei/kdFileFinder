'''
Created on 2019年3月26日

@author: bkd
'''
from os import remove
class delete:
    def execute(self,cur_item,script_variable):
        remove(cur_item)
        print("删除文件成功" + cur_item)