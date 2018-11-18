import sys, subprocess, re

class UnsupportedOsError(Exception): 
    def __init__(self):
        super().__init__('This method does not support current OS')

def get_fileinfo(file_path):
    if not sys.platform.startswith('win'): # only on linux/OS X systems
        output = subprocess.Popen(['file', file_path], stdout=subprocess.PIPE).communicate()[0]
        return output.decode().strip()
    else: raise UnsupportedOsError

def find_flag(regex, file_path):
    file = open(file_path, 'rb')
    data = file.read().decode('utf-8')
    p = re.compile(regex)
    return p.findall(data)
