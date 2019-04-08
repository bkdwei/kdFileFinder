import configparser
import json
from .fileutil import check_and_create,get_file_realpath

# config_file = os.path.join(os.path.expanduser('~') , ".config/kdFileFinder/config.ini")
config_file = get_file_realpath("data/config.ini")
check_and_create(config_file)
cf = configparser.ConfigParser()
cf.read(config_file,encoding="utf-8")

def list_add(section, option, value):
    option_list = init_list(section, option)
    option_list.append(value)
    cf.set(section, option, json.dumps(option_list,ensure_ascii=False))
    with open(config_file,"w",encoding="utf-8") as f:
        cf.write(f)
def list_del(section, option, value):
    option_list = init_list(section, option)
    option_list.remove(value)
    cf.set(section, option, json.dumps(option_list,ensure_ascii=False))
    with open(config_file,"w",encoding="utf-8") as f:
        cf.write(f)
def init_list(section,option):
    if not cf.has_section(section) :
        cf.add_section(section)
    option_list = []
    if cf.has_option(section, option):
        string_option = cf.get(section, option)
        if  string_option:
            option_list = json.loads(string_option)
    return option_list
def dict_add(section, option, value):
    option_dict = init_dict(section, option)
    option_dict.update(value)
    cf.set(section, option, json.dumps(option_dict,ensure_ascii=False))
    with open(config_file,"w",encoding="utf-8") as f:
        cf.write(f)
def init_dict(section,option):
    if not cf.has_section(section) :
       cf.add_section(section)
    option_dict = {}
    if cf.has_option(section, option):
        string_option = cf.get(section, option)
        if  string_option:
            option_dict = json.loads(string_option)
    return option_dict