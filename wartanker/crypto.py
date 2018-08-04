import base64, string

def b64encode(string, encoding='UTF-8'):
    return base64.b64encode(bytes(string, encoding)).decode()
