'''
Created on 2019年3月26日

@author: bkd
'''
from shutil import make_archive as ma
from os.path import join, dirname,isfile,normpath
from os import chdir,walk
import zipfile

class make_archive:
    def execute(self,script_variable):
        cur_path = script_variable["cur_path"]
        cur_file = script_variable["file_list"][0]
        cur_item = join(cur_path,cur_file)
#         ma(cur_item,"zip",root_dir=cur_item)
        print("压缩:" + cur_item )
#         chdir(cur_path)
        #ma(cur_item,"zip",root_dir=cur_item,base_dir=cur_path)
        filelist = []
        if isfile(cur_item):
            filelist.append(cur_item)
        else :
            filelist.append(cur_item)
            for root, dirs, files in walk(cur_item):
                for d in dirs:
                    filelist.append(normpath(join(root,d)))
                for name in files:
                    filelist.append(normpath(join(root, name)))
    
        zf = zipfile.ZipFile(cur_item  + ".zip", "w", zipfile.zlib.DEFLATED)
        for tar in filelist:
            arcname = tar[len(cur_path):]
            #print arcname
            zf.write(tar,arcname)
        zf.close()