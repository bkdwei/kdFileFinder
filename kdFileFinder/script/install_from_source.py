'''
Created on 2019年3月26日

@author: bkd
'''

from os import chdir,system
from os.path import exists,join
class install_from_source:
    def execute(self,script_variable):
        if exists(join(script_variable["cur_path"],"setup.py")) :
            chdir(script_variable["cur_path"])
            system("python setup.py install")
