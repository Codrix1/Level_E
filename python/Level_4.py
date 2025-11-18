def ans_1():
    def reverse(string):
        reverse = ""
        for i in range (len(string)-1 , -1 , -1):
            reverse += string[i]
        return reverse
    string = "rekcah_repus"
    print(reverse(string))
    return

def ans_2():
    password = input("Enter password for checking: ")
    if len(password) < 8:
        print("week password less than 8 letters")
        return
    for i in "!@#$%^&*()_+-=":
        if i in password:
            break
        if i == "=":
            print("password doesnt have a special character")
            return
    for i in "1234567890":
        if i in password:
            break
        if i == "0":
            print("password doesnt have a number")
            return
    print("strong password")
    return

import string
import random
def ans_3():
    length = int(input("Enter password length: "))

    characterList = ""
    characterList += string.ascii_letters
    characterList += string.digits
    characterList += string.punctuation

    password = []

    for i in range(length):
        randomchar = random.choice(characterList)
        password.append(randomchar)
    print("The random password is " + "".join(password))
    return

import hashlib

def ans_4():
    string = input("enter the string to be hashed: ")
    encoded = string.encode()
    md5 = hashlib.md5()
    md5.update(encoded)
    hashed = md5.hexdigest()
    print(hashed)
    return


def ans_5():
    ip = "192.168.190.36"
    spliting = ip.split(".")
    if len(spliting) > 4:
        print("invalid ip")
    for i in spliting:
        if i[0] == "0":
            print("invalid ip")
            return 
        try: 
            value = int(i)
            if not (value > -1 and value < 256) :
                print("invalid decimal value")
                return
        except:
            print("not a number")
            return
    print("valid ip")

def ans_6():
    digits = "0123456789ABCDEF"
    mac=""
    for i in range(0,6):
        if i > 0:
            mac+=":"
        mac += random.choice(digits)
        mac += random.choice(digits)
    print(mac)
    return

def ans_7():
    
    string = input("enter the string to be hashed: ").encode()
    key = "jasd;ofj234-23rhery8fh324l;kdj".encode()
    cipher = ""
    a = 0
    for i in range(0, len(string)):
        cipher+= str(key[a] ^ string[i])
        if(a < len(key)-2):
            a+=1
        else: 
            a = 0

    print(cipher)
    return

import uuid
def ans_8():
    device = uuid.uuid4()
    return

def ans_10():
    string = input("enter string to extract vowels form: ")
    count = {}
    for i in string:
        if i in "aeiouAEIOU":
            if i in count:
                count[i]+=1
            else:
                count[i] = 1
    print(count)
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