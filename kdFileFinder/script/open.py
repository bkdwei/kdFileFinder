'''
Created on 2019年3月26日

@author: bkd
'''
try:
    from os import startfile
except Exception as e:
    pass
from sys import platform
from os import system
class open:
    def execute(self,script_variable):
        if platform =="win32":
            startfile(script_variable["cur_item"])
        else:
            system('x-terminal-emulator --working-directory={} &'.format(script_variable["cur_item"]))
