'''
Created on 2019年3月24日

@author: bkd
'''
import json
from .kdconfig import cf
def get_bookmark():
    if cf.has_option("global", "bookmark"):
        string_bookmark = cf.get("global", "bookmark")
        return set(json.loads(string_bookmark))
        