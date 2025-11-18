def ans_1():
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

def ans_2():
    port = input("enter the port to check: ")
    if port >= 0 and port <= 65535:
        print("valid range")
    else:
        print("invalid")
    return 

import socket


def scan_ports(hostip , startport , endport):
    for port in range(startport , endport+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  
        
        result = sock.connect_ex((hostip, port))
        if result == 0:
            print(f"Port {port} is open")

        sock.close()

def ans_3():
    target_hosts = input("Enter the host IP address: ")
    scan_ports(target_hosts, 1, 1000)
    return


def check_tcp(host: str, port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((host, port))
    print(f"TCP connect_ex result: {result}")
    sock.close()
    return result == 0


def check_udp(host: str, port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(2)
    try:
        result = sock.connect_ex((host, port))
        print(f"UDP connect_ex result: {result}")
        return result == 0
    finally:
        sock.close()


def ans_4():
    ip_port = input("Enter the ip:port → ")
    ip, port = ip_port.split(":")
    port = int(port)

    if check_tcp(ip, port):
        print("TCP port is open (connect_ex returned 0)")
    else:
        print("TCP port is closed or filtered")

    if check_udp(ip, port):
        print("UDP port appears open (not reliable check)")
    else:
        print("UDP port likely closed or unreachable")
    
import random

def ans_5():
    host = input("Enter the IP or hostname: ")
    print("Testing 5 random ports between 1024 and 65535...")

    for i in range(5):
        port = random.randint(1024, 65535)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        s.close()

        if result == 0:
            print(f"Port {port} is OPEN!")
        else:
            print(f"Port {port} is closed.")    

def ans_6():
    port = int(input("Enter a port number: "))
    if port >= 0 and port <= 1023:
        print("This port is in the privileged range.")
    else:
        print("This port is not in the privileged range.")
    return

def ans_7():
    print("Checking all listening ports on 127.0.0.1...")
    for port in range(1, 1024):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex(("127.0.0.1", port))
        if result == 0:
            print(f"Port {port} is listening.")
        s.close()
    return

def ans_8():
    ip = input("Enter target IP: ")
    start = int(input("Enter start port: "))
    end = int(input("Enter end port: "))
    print("Starting TCP port scan...")
    for port in range(start, end + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"TCP Port {port} is open")
        s.close()
    return

def ans_9():
    ip = input("Enter target IP: ")
    start = int(input("Enter start port: "))
    end = int(input("Enter end port: "))
    print("Starting UDP port scan...")
    for port in range(start, end + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"UDP Port {port} might be open")
        s.close()
    return

def ans_10():
    print("Commonly used reserved ports in hacking:")
    ports = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        111: "RPCbind",
        135: "MS RPC",
        139: "NetBIOS",
        143: "IMAP",
        161: "SNMP",
        389: "LDAP",
        443: "HTTPS",
        445: "SMB",
        512: "exec",
        513: "login",
        514: "shell",
        873: "rsync",
        995: "POP3S"
    }
    for port, name in ports.items():
        print(f"Port {port} - {name}")
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
    # ans_10()
    return


if __name__ == "__main__":
    main()