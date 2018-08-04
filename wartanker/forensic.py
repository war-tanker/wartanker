import os
import re

def get_fileinfo(file_path):
    return os.system('file ' + path)    

def find_flag(regex, file_path):
    file = open(file_path, 'r')
    data = file.read()
    p = re.compile(regex)
    print p.findall(data)