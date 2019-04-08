'''
Created on 2019年4月8日

@author: bkd
'''
from traceback import format_exception
import sys
from PyQt5.QtWidgets import QMessageBox

class global_exception_hander:
    def new_except_hook(self,etype, evalue, tb):
        print(''.join(format_exception(etype, evalue, tb)))
        QMessageBox.information(None, 
                                      str('error'),
                                      ''.join(format_exception(etype, evalue, tb)))
        sys.exit()
    
#     注册全局异常处理类
    def patch_excepthook(self):
        sys.excepthook = self.new_except_hook