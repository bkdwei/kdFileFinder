'''
Created on 2019年3月26日

@author: bkd
'''
from shutil import make_archive as ma
class make_archive:
    def execute(self,script_variable):
        cur_item = script_variable["cur_item"]
        ma(cur_item,"zip",root_dir=cur_item)