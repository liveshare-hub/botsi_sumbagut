import random
import time
import hashlib

def generateUniqueCode():
    t = int(time.time() * 10000)
    r = int(random.random() * 1000000000000)
    a = random.random() * 1000000000000
    data = (str(t)+' '+str(r)+' '+str(a)).encode('utf-8')
    data = hashlib.md5(data).hexdigest()

    return data

def listTostring(s):
    str1 = " "
    
    return (str1.join(s))