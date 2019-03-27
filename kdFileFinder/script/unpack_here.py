'''
Created on 2019年3月27日

@author: bkd
'''
from shutil import unpack_archive
class unpack_here:
    def execute(self,script_variable):
        cur_item = script_variable["cur_item"]
        unpack_archive(cur_item,extract_dir=script_variable["cur_path"])