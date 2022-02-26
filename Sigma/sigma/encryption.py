from hashlib import sha256

def check(a,b):
    if (sha256(a.encode).hexdigest() == sha256(b.encode).hexdigest()):
        return True
    else:
        return False
def encrypt(a):
    return sha256(a.encode).hexdigest()