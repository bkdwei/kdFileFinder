'''
Created on 2019年3月26日

@author: bkd
@summary: 自动部署车检项目到生产环境
'''
from os import rename,system
from os.path import join,exists,splitext,basename
from shutil import unpack_archive ,copy2,rmtree
from PyQt5.QtWidgets import QMessageBox
class auto_deploy_carCheck(QMessageBox):
    def execute(self,script_variable):
        self.deploy_path = "E:\\tmpwork\\webapps\\"
        cur_item= script_variable["cur_item"]
        cur_path= script_variable["cur_path"]
        
#         self.setWindowTitle("自动部署车检项目到生产环境")
#         防止界面一闪而过
#         script_variable["auto_deploy_carCheck_dialog"] = self
        
#         t1 = threading.Thread(target=self.run_thread,args=(cur_item,cur_path) )
        self.run_thread(cur_item, cur_path)
#         system('taskkill /IM java.exe /F')
#         print("关闭tomcat成功")
#         
#         self.unpack(cur_item,cur_path)
#         self.rename()
#         self.copy_properties(cur_path)
        
        
#         t1.setDaemon(True)
#         t1.start()
#         解压
#         self.setLabelText("部署完毕 ")
#         self.setValue(100)
        
#         self.show()

    def unpack(self,cur_item,cur_path):
        unpack_archive(cur_item,extract_dir=self.deploy_path)
#         self.setLabelText("解压完毕" )
#         self.setValue(20)
#         self.show()
        print("解压完毕")
        
    def rename(self,cur_item):
        if exists(join(self.deploy_path,"ROOT")) : 
            rmtree(join(self.deploy_path,"ROOT"))
            print("删除旧目录成功，" + join(self.deploy_path,"ROOT") )
        print(splitext(basename(cur_item))[0])
        rename(join(self.deploy_path,splitext(basename(cur_item))[0]),join(self.deploy_path,"ROOT"))
        print("重命名文件夹成功")
#         t2 = threading.Thread(target=self.copy_properties,args=(cur_path,) )
#         t2.start()
#         t2.join()
    def copy_properties(self,cur_path):
#         self.setLabelText("正在复制jeesite.properties")
#         self.setValue(30)
#         self.show()
        print("正在复制jeesite.properties")
        copy2(join(cur_path,"jeesite.properties"),join(self.deploy_path,"ROOT\\WEB-INF\\classes\\"))
        print("正在复制mongodb.properties")
        copy2(join(cur_path,"mongodb.properties"),join(self.deploy_path,"ROOT\\WEB-INF\\classes\\"))
#         self.close()
        print("复制配置文件成功")
    def run_thread(self,cur_item,cur_path):
        system('taskkill /IM java.exe /F')
        print("关闭tomcat成功")
        
        self.unpack(cur_item,cur_path)
        self.rename(cur_item)
        self.copy_properties(cur_path)
        QMessageBox.information(self, "自动部署车检项目到生产环境",   "部署完毕", QMessageBox.Ok)
