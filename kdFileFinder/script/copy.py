'''
Created on 2019年3月26日

@author: bkd
'''
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl,QMimeData
from os.path import join

class copy:
    def execute(self,script_variable):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        if mimeData.hasUrls():
            print("准备粘贴:" + clipboard.text(),mimeData.formats())
            urls = mimeData.urls()
            for url in urls:
                print("mimeData:" ,url.url() )
            path = clipboard.text()
            item = {}         
            
        cur_path = script_variable["cur_path"]
        file_list = script_variable["file_list"]
        print("in copy ",file_list)
        urls = [ ]
        for file in file_list :
#             url = QUrl(join(cur_path,file.strip()).replace("%5C",""))
            url = QUrl("file:///" + cur_path + "/" +file)
#             url.set
            urls.append(url)
        mimeData = QMimeData()
#         mimeData.setUrls(urls)
#         mimeData.setData("text/uri-list",str("file:///E:/tmpwork/kdssh").encode())
        files1 = ["file:///" +  cur_path + "/" + f for f in file_list]
        files = "\n".join(files1)
        mimeData.setData("text/uri-list",files.encode())
        
        clipboard.setMimeData(mimeData)
#         

# QClipboard* cb = QApplication::clipboard();
# QDir dir("contracts/" + item->text(0));
# 
# QMimeData* mimeData = new QMimeData();
# mimeData->setData("text/uri-list",QString("file:///" + dir.absolutePath()).toLatin1());
# cb->setMimeData(mimeData);