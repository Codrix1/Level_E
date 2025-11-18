



from ipaddress import IPv4Address, IPv4Network, ip_address
import re


def ans_1():
    def validateipv4(addresslist):
        for section in addresslist:
            if section.isdigit():
                numeric = int(section)
                if numeric < 0  or numeric > 255:
                    return print("invalid ipv4 address")
            else:
                return print("invalid ipv4 address")  
            
        if len(addresslist) != 4:
            return print ("invalid ipv4 address")  
        return print("valid ipv4 address")
    
    def checkHex(s):
        return bool(re.match(r'^[0-9a-fA-F]*$', s))

    def validateipv6(addresslist):
        for section in addresslist:
            if not checkHex(section):
                return print("invalid ipv6 address")
            
        if len(addresslist) != 8:
            return print ("invalid ipv6 address")  
        return print("valid ipv6 address")
        
    address = input("enter the ip address you wish to classify \n")

    if "." in address:
        addresslist = address.split(".")
        validateipv4(addresslist)

    elif ":" in address:
        addresslist = address.split(":")
        validateipv6(addresslist)
    else:
        print("this isnt an ip address \n")
    
    return 


def ans_2():

    def convertipv4(addresslist):
        binaddress=""
        for section in addresslist:
            if section.isdigit():
                numeric = int(section)
                if numeric < 0  or numeric > 255:
                    return print("invalid ipv4 address")
                binaddress += (str(bin(numeric)[2:].zfill(8)) +" ")
            else:
                return print("invalid ipv4 address")  
            
        if len(addresslist) != 4:
            return print ("invalid ipv4 address")  
        return print(f"converted ipv4 address: {binaddress}")
    
    address = input("enter the ipv4 address you wish to convert \n")

    if "." in address:
        addresslist = address.split(".")
        convertipv4(addresslist)
    else:
        return print("invalid ipv4 address")


    return

def ans_3():
    with open("E:\\hacking study\\Level_E\\network\\testfile.txt") as fh:
        fstring = fh.readlines()
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

    lst=[]

    for line in fstring:
        match = pattern.search(line)
        if match:
            lst.append(match.group(0))
    
    print(lst)

    return

def ans_4():
    def convertipv4(addresslist):
        binaddress = ""

        for section in addresslist:
            if section.isdigit():
                numeric = int(section)
                if numeric < 0 or numeric > 255:
                    print("invalid ipv4 address")
                    return
                binaddress += (str(numeric) +".")
            else:
                print("invalid ipv4 address")
                return

        if len(addresslist) != 4:
            print("invalid ipv4 address")
            return

        first, second = int(addresslist[0]), int(addresslist[1])

        if first == 10:
            print(f"{binaddress} is a private ip")
        elif first == 172 and 16 <= second <= 31:
            print(f"{binaddress} is a private ip")
        elif first == 192 and second == 168:
            print(f"{binaddress} is a private ip")
        else:
            print(f"{binaddress} is a public ip")

    address = input("enter the ipv4 address you wish to check \n")

    if "." in address:
        addresslist = address.split(".")
        convertipv4(addresslist)
    else:
        print("invalid ipv4 address")


def network(ip , mask):
    brod = []
    for i in range(0 , 4):
        if i < len(mask):
            res = ip[i] & mask[i]
        else:
            res = ip[i]
        brod.append(res)
        
    print(f"network: {brod}")
    return brod
def broadcast(ip , mask):
    brod = []
    for i in range(0 , 4):
        if i < len(mask):
            res = ip[i] | (255 - mask[i])
        else:
            res = ip[i]
        brod.append(res)
        
    print(f"broadcast: {brod}")
    return brod
def calcmask(mask): 
    res = []
    itr = 0
    while itr < mask:
        start = itr
        num = 0 
        i = 7 
        while num < 255 and start < mask:
            num += 2 ** i
            i -= 1
            start += 1
            itr += 1
        res.append(num)
    while len(res) < 4:
        res.append(0)
    print(f"the bin mask is: {res}")  
    return res  

def ans_5():
    def extractIpAndMask(addresslist):
        binaddress=[]
        last = addresslist[3].split("/")

        for section in addresslist:
            if section.isdigit():
                numeric = int(section)
            else:
                numeric = int(last[0])
            binaddress.append(numeric)
        mask = str(last[1])
        masklist = calcmask(int(mask))
        print(binaddress)
        if len(addresslist) != 4:
            return print ("invalid ipv4 address")  
        return binaddress , masklist
    

    address = input("enter the ipv4 address you wish to use \n")

    if "." in address:
        addresslist = address.split(".")
        ipadd , mask = extractIpAndMask(addresslist)
        broadcast(ipadd, mask)
        network(ipadd , mask)
        print (f"ip address = {ipadd} , mask = {mask}" )
    else:
        return print("invalid ipv4 address")
    return

from netaddr import *

def ans_6():
    address = input("enter the CIDR you wish to use: ")
    ip = IPNetwork(address)
    iplist = list(ip)
    print(len(ip))
    for i in range(0,len(ip)) :
        print(str(iplist[i]))
    return

from pythonping import ping

def ans_7():
    address = input("enter the ipv4 address you wish to ping: ")
    ping(address, verbose=True)
    return
        
def ans_8():
    address = input("enter the ipv6 you wish to use: ")
    option = input("Expand = 1 or Compress = 0 : ")
    ip = ip_address(address)
    if option == "1":
        print(ip.exploded)
    if option == "0":
        print(ip.compressed)
    return

def ans_9():
    classA = IPv4Network("10.0.0.0/8")
    classB = IPv4Network("172.16.0.0/12")
    classC = IPv4Network("192.168.0.0/16")
    classD = IPv4Network("224.0.0.0/4")  
    classE = IPv4Network("240.0.0.0/4") 

    address = IPv4Address(input("enter the ipv4 address you wish to identify: "))

    if address in classA:
        print("ip in class A")
    elif address in classB:
        print("ip in class B")
    elif address in classC:
        print("ip in class C")
    elif address in classD:
        print("ip in class D")
    elif address in classE:
        print("ip in class E")
    else:
        print("ip not in class A-E")
    
    return


def ans_10():
    
    def extractIpAndMask(addresslist):
        binaddress=[]
        last = addresslist[3].split("/")

        for section in addresslist:
            if section.isdigit():
                numeric = int(section)
            else:
                numeric = int(last[0])
            binaddress.append(numeric)
        mask = str(last[1])
        masklist = calcmask(int(mask))
        print(binaddress)
        if len(addresslist) != 4:
            return print ("invalid ipv4 address")  
        return binaddress , masklist

    address1 = input("enter the first address you wish to use \n")
    address2 = input("enter the second address you wish to use \n")

    if "." in address1:
        addresslist = address1.split(".")
        ipadd , mask = extractIpAndMask(addresslist)
        broad1 = broadcast(ipadd, mask)
        network1 = network(ipadd , mask)
        print (f"ip address = {ipadd} , mask = {mask}" )
    else:
        return print(f"invalid ipv4 address: {address1}")
    
    if "." in address2:
        addresslist = address2.split(".")
        ipadd , mask = extractIpAndMask(addresslist)
        broad2 = broadcast(ipadd, mask)
        network2= network(ipadd , mask)
    else:
        return print(f"invalid ipv4 address: {address1}")
    

    if broad1 == broad2 and network1 == network2:
        print("both are in the same subnet")

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
    ans_9()
    # ans_10()
    return


if __name__ == "__main__":
    main()