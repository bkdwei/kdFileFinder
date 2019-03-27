'''
Created on 2019年3月27日

@author: bkd
'''
from shutil import unpack_archive
from os.path import splitext,basename, join
class unpack_to_same_dir:
    def execute(self,script_variable):
        cur_item = script_variable["cur_item"]
        unpack_archive(cur_item,extract_dir=join(script_variable["cur_path"],splitext(basename(cur_item))[0]))