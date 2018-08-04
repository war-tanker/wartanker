import hashlib

md5 = hashlib.md5()
sha = hashlib.sha()
sha1 = hashlib.sha1()
sha224 = hashlib.sha224()
sha256 = hashlib.sha256()
sha384 = hashlib.sha384()
sha512 = hashlib.sha512()

def get_hashtype(string):
    

def md5encode(string):
    return md5.update(string).hexdigest()

def shaencode(string):
    return sha.update(string).hexdigest()

def sha1encode(string):
    return sha1.update(string).hexdigest()

def sha256encode(string):
    return sha256.update(string).hexdigest()

def sha384encode(string):
    return sha384.update(string).hexdigest()

def sha512encode(string):
    return sha512.update(string).hexdigest()

def sha_encode(sha, string):
    return eval('hashlib.sha' + str(sha) + '().update(' + string + ').hexdigest()')
    
