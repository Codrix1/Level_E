def ans_1():
    list = [
    "Nmap",
    "Wireshark",
    "Metasploit Framework",
    "Aircrack-ng",
    "John the Ripper",
    "Hydra",
    "Burp Suite",
    "Nikto",
    "sqlmap",
    "Hashcat"
    ]
    return list

def ans_2():
    print(ans_1()[2])
    return

def ans_3():
    status_codes = {
    200: "OK",
    201: "Created",
    204: "No Content",
    301: "Moved Permanently",
    302: "Found",
    304: "Not Modified",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    408: "Request Timeout",
    409: "Conflict",
    429: "Too Many Requests",
    500: "Internal Server Error",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout"
    }
    return status_codes

def ans_4():
    string = input("enter string: ")
    count = {}
    for i in string:
        if i in count:
            count[i]+=1
        else:
            count[i] = 1
    print(count)
    return

def ans_5():
    def bubble_sort(numbers):
        n = len(numbers)
        for i in range(0,n-1):
            swapped = False
            for j in range(0 , n-i-1):
                if numbers[j] > numbers[j+1]:
                    numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
                    swapped = True
            if not swapped:
                break
        return array
    array = [3 ,34,5,56,78,2,12 ,24]
    print (bubble_sort(array))
    return

def ans_6():
    search = True
    ports = {
    20: "FTP (Data Transfer)",
    21: "FTP (Control)",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
    }
    while search:
        port = int(input("please enter the port number: "))
        if port in ports:
            print(ports[port])
        else:
            print("port doesnt exist")
        res = input("Search again [Y/n]: ")
        if res == 'n':
            search = False
                    
    return

def ans_7():
    array = [3, 34, 5, 56, 5, 3, 78, 2, 12, 56, 56, 24]
    new = []
    store = {}
    for i in array:
        if not i in store:
            new.append(i)
            store[i] = 1

    print(new)
    return

def ans_8():
    list = [1, 'apple', 3.14, 'banana']
    res = ', '.join(str(a) for a in list)
    print(res)

def ans_9():
    list = [ 'adljflasdoijew',1, 'apple', 3.14, 'banana']
    max = 0 
    word = ""
    for i in list:
        if len(str(i)) > max:
            max = len(str(i)) 
            word = i
    print(word)
    return

def ans_10():
    search = True
    users = {
    "alice": "pass123",
    "bob": "secure456",
    "charlie": "mypwd789",
    "diana": "letmein01",
    "eve": "qwerty99",
    "frank": "hello2025",
    "grace": "python321",
    "heidi": "testpass77",
    "ivan": "code654",
    "judy": "sample111"
    }
    while search:
        user = input("please enter the username: ")
        if user in users:
            print(users[user])
        else:
            print("user doesnt exist")
        res = input("Search again [Y/n]: ")
        if res == 'n':
            search = False
def main():
    ans_1()
    # ans_2()
    # ans_3()
    # ans_4()
    # ans_5()
    # ans_6()    
    # ans_7()
    # ans_8()
    # ans_9()
    # ans_10()

 
if __name__ == "__main__":
    main()