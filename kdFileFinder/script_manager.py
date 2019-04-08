'''
Created on 2019年3月25日

@author: bkd
'''
import importlib
from os.path import splitext, dirname
from PyQt5.QtWidgets import  QDialog,QListWidgetItem,QAction, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot,pyqtSignal
from .fileutil import get_file_realpath
from .customer_script import customer_script
from . import kdconfig

class script_manager(QDialog):
    show_script_result_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        loadUi(get_file_realpath("script_manager.ui"), self)
        self.cs = customer_script()
        self.init_dict()
        
#         存放脚本的临时变量
        self.temp_variable ={}
    def init_dict(self):
        self.script_dict = kdconfig.init_dict("script", "customer_script")
        sc_items = self.script_dict.items()
        for sc in sc_items:
            list_item = QListWidgetItem(sc[0])
            list_item.setData(-1,sc[1])
            self.lv_script.addItem(list_item)
        self.lv_script.itemDoubleClicked.connect(self.on_lv_script_itemDoubleClicked)
    @pyqtSlot()
    def on_pb_add_script_clicked(self):
        reply = self.cs.exec_()
        if reply:
            print(self.cs.bg_apply_type.checkedButton().text())
            self.script_dict[self.cs.le_name.text()] = {"path":self.cs.le_path.text(),"apply_type":self.cs.bg_apply_type.checkedButton().apply_type,"filetype":self.cs.le_filetype.text()}
            kdconfig.dict_add("script", "customer_script", self.script_dict)
            print(self.script_dict)
            
    @pyqtSlot()
    def on_lv_script_itemDoubleClicked(self):
        cur_item = self.lv_script.currentItem()
        script = cur_item.data(-1)
        script["name"] =cur_item.text()
        self.cs.edit(script)
        self.on_pb_add_script_clicked()
         
    def loadPlugin(self, filename,filePath):
        print("loading plugin:" + 'kdFileFinder.script.' + splitext(filename)[0])
#         plugin=__import__(get_file_realpath("script/"+filename), fromlist=[filename],level=0)
        
        script_module = importlib.import_module('kdFileFinder.script.' + splitext(filename)[0])
        script_class = getattr(script_module,splitext(filename)[0])
#         plugin=__import__("menu")
#         clazz=plugin.getPluginClass()
        o=script_class()
#         o.setFather(self, self.kdpad)
        self.temp_variable["cur_path"] = dirname(filePath)
        self.temp_variable["cur_item"] = filePath
        try:
            o.execute(self.temp_variable)
        except Exception as e:
            print("检测异常",e)
            QMessageBox.information(self, "系统异常",   str(e), QMessageBox.Ok)
#         if self.script_variable["script_result_body"] :
        print("temp_variable:" , self.temp_variable)
#             QMessageBox.information(self,"粘贴文件",self.script_variable["script_result_body"])
#             self.show_script_result_signal.emit(self.script_variable["statusbar_msg"])
    def get_file_menu_item(self):
            sc_items = self.script_dict.items()
            actions = set()
            for sc in sc_items:
                if sc[1]["apply_type"] == 1:
                    action = QAction(sc[0])
                    actions.add(action)
            return actions
    def run_script(self,script_name,filePath):
        script_path = self.script_dict[script_name]["path"]
        print("script_path:" + script_path)
        self.loadPlugin(script_path,filePath)
