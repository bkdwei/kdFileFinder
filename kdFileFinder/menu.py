'''
Created on 2019年3月25日

@author: bkd
'''
from PyQt5.QtWidgets import QAction
from .script_manager import script_manager

# dl_script_manage = script_manager()
class toolbar_menu:
    menu_item = [QAction("脚本管理"),QAction("新建"), QAction("粘贴"),QAction("复制")]
    def __init__(self):
        super().__init__()
        self.dl_script_manage = script_manager()
    def handle_action(self,action):
        text = action.text()
        if text == "脚本管理":
            print("脚本管理")
            self.dl_script_manage.exec_()

class file_menu:
    def __init__(self):
        super().__init__()
        self.dl_script_manage = script_manager()
        self.menu_item = self.dl_script_manage.get_file_menu_item()
    def get_menu_list(self):
        pass
    def handle_action(self,action,filePath):
        text = action.text()
        self.dl_script_manage.run_script(text,filePath)
