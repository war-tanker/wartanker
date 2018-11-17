import hashlib

def md5encode(string):
    md5 = hashlib.md5()
    md5.update(string.encode('utf-8'))
    return md5.hexdigest()

def sha1encode(string):
    sha1 = hashlib.sha1()
    sha1.update(string.encode('utf-8'))
    return sha1.hexdigest()

def sha256encode(string):
    sha256 = hashlib.sha256()
    sha256.update(string.encode('utf-8'))
    return sha256.hexdigest()

def sha384encode(string):
    sha384 = hashlib.sha384()
    sha384.update(string.encode('utf-8'))
    return sha384.hexdigest()

def sha512encode(string):
    sha512 = hashlib.sha512()
    sha512.update(string.encode('utf-8'))
    return sha512.hexdigest()

def sha_encode(sha, string):
    sha = int(sha)
    if sha==1:
        sha_=hashlib.sha1()
    elif sha==256:
        sha_=hashlib.sha256()
    elif sha==384:
        sha_=hashlib.sha384()
    elif sha==512:
        sha_=hashlib.sha512()
    sha_.update(string.encode('utf-8'))
    return sha_.hexdigest()
