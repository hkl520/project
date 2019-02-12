import os
import yaml

def read_yaml_data(file_name):
    with open(os.getcwd()+os.sep+"data" + os.sep + file_name,'r',encoding='utf-8') as f:
      return yaml.load(f)
