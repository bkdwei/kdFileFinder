'''
Created on 2019年3月26日

@author: bkd
'''

from os import chdir,system
from os.path import exists,join
class build_source_distribute:
    def execute(self,script_variable):
        if exists(join(script_variable["cur_path"],"setup.py")) :
            chdir(script_variable["cur_path"])
            system("python setup.py sdist")
