'''
Created on 2019年3月26日

@author: bkd
'''
from shutil import make_archive as ma
from os.path import join

class make_archive:
    def execute(self,script_variable):
        cur_item = join(script_variable["cur_path"],script_variable["file_list"][0])
#         ma(cur_item,"zip",root_dir=cur_item)
        ma(cur_item,"zip")