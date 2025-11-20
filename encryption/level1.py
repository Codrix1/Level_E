def ans_1():
    string = "encode"
    encoded = string.encode("utf-8")
    decoded = encoded.decode("utf-8")
    print(encoded)
    print(decoded)
    return


def ans_2():
    string = 890
    hexdecimal = hex(string)
    print(hexdecimal)
    return

import hashlib

def ans_3():
    file_name = 'encryption\\level2.py'
    with open(file_name, 'rb') as file_to_check:
        data = file_to_check.read()    
        md5_returned = hashlib.md5(data).hexdigest()
        print (md5_returned)
    return

def ans_4():
    string = 'testing the sha encoding'

    hash = hashlib.sha1(string.encode("utf-8")).hexdigest()
    print (hash)
    return

def ans_5():
    password = input("enter the pasword you want to hash: ")
    hash = hashlib.sha1(password.encode("utf-8")).hexdigest()
    print (hash)
    return

def ans_6():
    file_name = 'encryption\\level2.py'
    with open(file_name, 'rb') as file_to_check:
        data = file_to_check.read()    
        hash1 = hashlib.sha256(data).hexdigest()

    file_name = 'encryption\\level3.py'
    with open(file_name, 'rb') as file_to_check:
        data = file_to_check.read()    
        hash2 = hashlib.sha256(data).hexdigest()
    
    if hash1 == hash2:
        print("passed integrity check")
    else:
        print("failed integrity check")
    
    return

def ans_7():
    for i in range(10000):
        pin = str(i).zfill(4)  
        digest = hashlib.md5(pin.encode()).hexdigest()
        print(digest)

    return

import base64


def ans_8():
    string = "testing"
    b64 = base64.b64encode(string.encode("utf-8")).decode("utf-8")
    print(b64)
    return

import binascii
import re

def detect_encoding(s):
    if re.fullmatch(r"[0-9a-fA-F]+", s) and len(s) % 2 == 0:
        try:
            binascii.unhexlify(s)
            return "hex"
        except:
            pass

    if len(s) % 4 == 0 and re.fullmatch(r"[A-Za-z0-9+/=]+", s):
        try:
            base64.b64decode(s, validate=True)
            return "base64"
        except:
            pass

    return "neither"

def ans_9():
    text = input("write the text to check if it is base64 or hex: ")
    print(detect_encoding(text))
    return

def ans_10():
    text = input("enter the text you want to hash: ")
    hash = hashlib.sha1(text.encode("utf-8")).hexdigest()
    print (hash)
    hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
    print (hash)
    hash = hashlib.md5(text.encode("utf-8")).hexdigest()
    print (hash)
    return

def main():
    # ans_1()
    # ans_2()
    # ans_3()
    # ans_4()
    # ans_5()
    # ans_6()    
    # ans_7()
    # ans_8()
    # ans_9()
    ans_10()
    return


if __name__ == "__main__":
    main()