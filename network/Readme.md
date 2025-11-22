# NETWORKING

---

## LEVEL 1 — (file: level_1.py)
### Topics: IP Addresses & Subnetting, IPv4, IPv6, CIDR

---

### Q1. Validate whether an IP is IPv4 or IPv6
```python
def ans_1():
    # This function validates IPv4 by checking numeric ranges
    # It validates IPv6 by checking hex blocks
    address = input("enter the ip address you wish to classify \n")

    if "." in address:
        addresslist = address.split(".")
        # validateipv4() was originally here
        if len(addresslist) != 4:
            return print("invalid ipv4 address")
        for section in addresslist:
            if not section.isdigit() or not (0 <= int(section) <= 255):
                return print("invalid ipv4 address")
        return print("valid ipv4 address")

    elif ":" in address:
        addresslist = address.split(":")
        # validateipv6() + checkHex() originally here
        if len(addresslist) != 8:
            return print("invalid ipv6 address")
        for section in addresslist:
            if not re.match(r'^[0-9a-fA-F]+$', section):
                return print("invalid ipv6 address")
        return print("valid ipv6 address")

    else:
        print("this isn't an ip address")
```

---

### Q2. Convert IPv4 dotted decimal to binary
```python
def ans_2():
    # Converts each octet to 8-bit binary
    address = input("enter the ipv4 address you wish to convert \n")

    if "." in address:
        addresslist = address.split(".")
        binaddress = ""
        for section in addresslist:
            if section.isdigit() and 0 <= int(section) <= 255:
                binaddress += bin(int(section))[2:].zfill(8) + " "
            else:
                return print("invalid ipv4 address")
        print(f"converted ipv4 address: {binaddress}")
    else:
        print("invalid ipv4 address")
```

---

### Q3. Extract all IP addresses from a text file
```python
def ans_3():
    # Reads a file, matches IPv4 patterns using regex
    with open("E:\\hacking study\\Level_E\\network\\testfile.txt") as fh:
        fstring = fh.readlines()

    pattern = re.compile(r'\d{1,3}(?:\.\d{1,3}){3}')
    lst = []

    for line in fstring:
        match = pattern.search(line)
        if match:
            lst.append(match.group(0))

    print(lst)
```

---

### Q4. Check if an IP belongs to a private network
```python
def ans_4():
    # Converts IP to octets and checks private ranges
    address = input("enter the ipv4 address you wish to check \n")

    if "." not in address:
        return print("invalid ipv4 address")

    addresslist = address.split(".")
    if len(addresslist) != 4:
        return print("invalid ipv4 address")

    first, second = int(addresslist[0]), int(addresslist[1])

    if first == 10:
        print("private IP")
    elif first == 172 and 16 <= second <= 31:
        print("private IP")
    elif first == 192 and second == 168:
        print("private IP")
    else:
        print("public IP")
```

---

### Q5. Calculate network & broadcast address from IP + mask
```python
def ans_5():
    # Calculates subnet mask from CIDR
    # Calculates network = ip & mask
    # Calculates broadcast = ip | ~mask
    address = input("enter the ipv4 address you wish to use (ex: 192.168.1.10/24)\n")

    if "." not in address:
        return print("invalid ipv4 address")

    parts = address.split("/")
    ip_raw = parts[0].split(".")
    cidr = int(parts[1])

    ip = list(map(int, ip_raw))

    mask = []
    bits = cidr
    for i in range(4):
        if bits >= 8:
            mask.append(255)
            bits -= 8
        else:
            val = (256 - (2 ** (8 - bits))) if bits > 0 else 0
            mask.append(val)
            bits = 0

    network = [ip[i] & mask[i] for i in range(4)]
    broadcast = [ip[i] | (255 - mask[i]) for i in range(4)]

    print("Network:", network)
    print("Broadcast:", broadcast)
```

---

### Q6. Generate all possible IPs in CIDR
```python
def ans_6():
    # Uses netaddr.IPNetwork to list all IPs
    address = input("enter the CIDR you wish to use: ")
    ip = IPNetwork(address)
    for host in ip:
        print(host)
```

---

### Q7. Check if an IP is reachable via ping
```python
def ans_7():
    # Uses pythonping to ping an IPv4 address
    address = input("Enter IP to ping: ")
    ping(address, verbose=True)
```

---

### Q8. Convert IPv6 to compressed / expanded
```python
def ans_8():
    # Converts IPv6 using ip_address()
    address = input("enter the ipv6 address: ")
    option = input("Expand = 1 | Compress = 0: ")

    ip = ip_address(address)
    print(ip.exploded if option == "1" else ip.compressed)
```

---

### Q9. Determine IPv4 class
```python
def ans_9():
    # Compares IPv4 against class ranges
    address = IPv4Address(input("enter the ipv4 address: "))

    if address in IPv4Network("10.0.0.0/8"):
        print("Class A")
    elif address in IPv4Network("172.16.0.0/12"):
        print("Class B")
    elif address in IPv4Network("192.168.0.0/16"):
        print("Class C")
    elif address in IPv4Network("224.0.0.0/4"):
        print("Class D")
    elif address in IPv4Network("240.0.0.0/4"):
        print("Class E")
    else:
        print("Not in class A–E")
```

---

### Q10. Check if two IPs are in the same subnet
```python
def ans_10():
    # Extracts mask, calculates network & broadcast for each IP
    ip1 = input("enter first IP/CIDR: ")
    ip2 = input("enter second IP/CIDR: ")

    def extract(ip):
        # helper function originally inside — validates IP and calculates mask
        parts = ip.split("/")
        ip_bytes = list(map(int, parts[0].split(".")))
        cidr = int(parts[1])

        mask = []
        bits = cidr
        for _ in range(4):
            if bits >= 8:
                mask.append(255)
                bits -= 8
            else:
                mask.append(256 - (2 ** (8 - bits)) if bits else 0)
                bits = 0
        return ip_bytes, mask

    ipA, maskA = extract(ip1)
    ipB, maskB = extract(ip2)

    netA = [ipA[i] & maskA[i] for i in range(4)]
    netB = [ipB[i] & maskB[i] for i in range(4)]

    if netA == netB:
        print("same subnet")
    else:
        print("different subnet")
```

---

## LEVEL 2 — (file: level_2.py)
### Topics: Ports & Protocols, TCP/UDP

---

### Q1. Print common ports and their services
```python
def ans_1():
    # Returns a dictionary of common HTTP/HTTPS/etc ports
    return {
        80: "HTTP",
        443: "HTTPS",
        21: "FTP",
        22: "SSH",
        25: "SMTP",
        110: "POP3",
        53: "DNS",
        23: "Telnet"
    }
```

---

### Q2. Check if a port number is valid
```python
def ans_2():
    # Ensures port is between 0 and 65535
    port = int(input("Enter port: "))
    print("valid" if 0 <= port <= 65535 else "invalid")
```

---

### Q3. Scan first 1000 ports
```python
def ans_3():
    # Performs a basic TCP scan using socket.connect_ex
    target = input("Enter target host: ")
    for port in range(1, 1001):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if s.connect_ex((target, port)) == 0:
            print(f"Port {port} open")
        s.close()
```

---

### Q4. Detect whether a port uses TCP or UDP
```python
def ans_4():
    # TCP and UDP checking using socket.connect_ex
    ip_port = input("Enter ip:port → ")
    ip, port = ip_port.split(":")
    port = int(port)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    print("TCP open" if s.connect_ex((ip, port)) == 0 else "TCP closed")
    s.close()

    u = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    u.settimeout(2)
    print("UDP maybe open" if u.connect_ex((ip, port)) == 0 else "UDP closed")
    u.close()
```

---

### Q5. Randomly generate and test 5 ports
```python
def ans_5():
    # Picks 5 random ports and tests if open
    host = input("Enter IP: ")
    for i in range(5):
        port = random.randint(1024, 65535)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if s.connect_ex((host, port)) == 0:
            print(f"Port {port} open")
        else:
            print(f"Port {port} closed")
        s.close()
```

---

### Q6. Check if port is privileged
```python
def ans_6():
    # Privileged ports = 0–1023
    port = int(input("Enter port: "))
    print("privileged" if 0 <= port <= 1023 else "not privileged")
```

---

### Q7. List all listening ports on localhost
```python
def ans_7():
    # Scans 1–1023 for open TCP ports
    for port in range(1, 1024):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex(("127.0.0.1", port)) == 0:
            print(f"Port {port} listening")
        s.close()
```

---

### Q8. Basic TCP Port Scanner
```python
def ans_8():
    # Simple TCP scanner using connect_ex
    ip = input("Enter target IP: ")
    start = int(input("Start port: "))
    end = int(input("End port: "))

    for port in range(start, end+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if s.connect_ex((ip, port)) == 0:
            print(f"TCP {port} open")
        s.close()
```

---

### Q9. Basic UDP Port Scanner
```python
def ans_9():
    # UDP scanner (not very reliable)
    ip = input("Enter target IP: ")
    start = int(input("Start port: "))
    end = int(input("End port: "))

    for port in range(start, end+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(1)
        if s.connect_ex((ip, port)) == 0:
            print(f"UDP {port} might be open")
        s.close()
```

---

### Q10. List common hacking-related reserved ports
```python
def ans_10():
    # Prints list of reserved + hacking-used ports
    ports = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        139: "NetBIOS",
        443: "HTTPS",
        445: "SMB",
        513: "login",
        514: "shell",
        873: "rsync"
    }
    for p, name in ports.items():
        print(f"{p} → {name}")
```

# Networking - Level 3

### Q1: Write a simple TCP client-server program that sends a message from client to server.

**Answer:**

* Implemented in **tcp_server.py** (TCP server) and **client.py** (TCP client).
* TCP server listens on port 5050 and handles multiple clients using threads.
* Client connects, sends a message, and prints handshake status.

**tcp_server.py**

```python
import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = "utf-8"
ADDR = (SERVER, PORT)
MAX_BYTES = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[CONNECTION ESTABLISHED] {addr}")
    connected = True

    while connected:
        msg = conn.recv(MAX_BYTES).decode(FORMAT)
        if msg == "syn":
            conn.send("syn,ack".encode(FORMAT))
            msg = conn.recv(MAX_BYTES).decode(FORMAT)
            if msg == "ack,bak":
                print("[TCP] Handshake successful.")
            else:
                print("[TCP] Handshake failed.")
            connected = False
        elif msg == "":
            connected = False

    conn.close()
    print(f"[DISCONNECTED] {addr}")

def start_server():
    server.listen()
    print(f"[LISTENING] TCP Server running on {SERVER}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]: {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
```

**client.py**

```python
import socket

PORT = 5050
SERVER = "192.168.0.26"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"

def connect_tcp():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client

def connect_udp():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect(ADDR)
    return client

def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)

def start():
    answer = int(input("Press 1 for TCP connection, 0 for UDP connection: "))

    match answer:
        case 0:
            connection = connect_udp()
            send(connection, "hi")
            print("[UDP] Message sent to server.")
        case 1:
            connection = connect_tcp()
            send(connection, "syn")
            msg = connection.recv(1024).decode(FORMAT)
            if msg == "syn,ack":
                send(connection, "ack,bak")
                print("[TCP] Handshake complete.")
            else:
                print("[TCP] Handshake failed.")
            connection.close()
        case _:
            print("Invalid option.")
            return

    print("Disconnected.")

if __name__ == "__main__":
    start()
```

---

### Q2: Modify the above program to work with UDP instead of TCP.

**Answer:**

* Implemented in **udp_server.py** (UDP server) and **client.py**.
* UDP server listens on port 5050 and echoes back “ack”.
* Client sends a message via UDP and prints confirmation.

**udp_server.py**

```python
import socket

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = "utf-8"
ADDR = (SERVER, PORT)
MAX_BYTES = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDR)

def start_server():
    print(f"[LISTENING] UDP Server running on {SERVER}:{PORT}")
    while True:
        msg, addr = server.recvfrom(MAX_BYTES)
        print(f"[UDP RECEIVED] {msg.decode(FORMAT)} from {addr}")
        server.sendto("ack".encode(FORMAT), addr)

if __name__ == "__main__":
    start_server()
```

---

### Q3: Create a TCP server that listens on port 9999 and responds with "Hello, Client!".

**Answer:**

* Implemented in **ans_3.py** (UDP implementation in provided code).

```python
import socket

PORT = 9999
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = "utf-8"
ADDR = (SERVER, PORT)
MAX_BYTES = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDR)

def start_server():
    print(f"[LISTENING] UDP Server running on {SERVER}:{PORT}")
    while True:
        msg, addr = server.recvfrom(MAX_BYTES)
        print(f"[UDP RECEIVED] {msg.decode(FORMAT)} from {addr}")
        server.sendto("Hello, Client!".encode(FORMAT), addr)

if __name__ == "__main__":
    start_server()
```

---

### Q4: Write a function that measures the round-trip time (RTT) of a TCP connection.

**Answer:**

* Implemented in **ans_4.py**.
* Connects to port 80 of a remote server and measures time.

```python
import socket
import time

def measure_rtt(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    start_time = time.time()
    sock.connect((address, 80))
    rtt = time.time() - start_time
    sock.close()
    return rtt

rtt = measure_rtt('google.com')
print(f"RTT: {rtt}s")
```

---

### Q5: Simulate a basic SYN flood attack (for controlled environments).

**Answer:**

* Implemented in **synflood.py**.
* Uses threads to simulate multiple TCP “SYN” messages to the server.

```python
import socket
import threading

PORT = 5050
SERVER = "192.168.0.26"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"

def connect_tcp():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client

def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)

def client():
    connection = connect_tcp()
    send(connection, "syn")
    msg = connection.recv(1024).decode(FORMAT)
    if msg == "syn,ack":
        print("connected.")
    return
    
def start():
    answer = int(input("enter the number of clients for the attack: "))
    for i in range(answer):
        thread = threading.Thread(target=client)
        thread.start()

if __name__ == "__main__":
    start()
```

---

### Q6: Write a script that monitors and logs all incoming TCP connections.

**Answer:**

* Implemented in **ans_6.py** using `psutil`.

```python
import psutil

def get_active_connections():
    connections = psutil.net_connections(kind='tcp')
    connection_details = []

    for conn in connections:
        local_address = f"{conn.laddr.ip}:{conn.laddr.port}"
        foreign_address = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
        state = conn.status
        pid = conn.pid
        process_name = None
        if pid:
            try:
                process = psutil.Process(pid)
                process_name = process.name()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                process_name = "N/A"

        connection_details.append({
            "Local Address": local_address,
            "Foreign Address": foreign_address,
            "State": state,
            "PID": pid,
            "Process Name": process_name,
        })

    return connection_details

def display_connections(connections):
    print(f"{'Local Address':<30} {'Foreign Address':<30} {'State':<15} {'PID':<10} {'Process Name':<25}")
    print("=" * 120)
    for conn in connections:
        print(f"{conn['Local Address']:<30} {conn['Foreign Address']:<30} {conn['State']:<15} {conn['PID']:<10} {conn['Process Name']}")

if __name__ == "__main__":
    active_connections = get_active_connections()
    display_connections(active_connections)
```

---

### Q7: Implement a TCP handshake simulation in Python.

**Answer:**

* Already implemented in **tcp_server.py** + **client.py**.
* The handshake is simulated with `"syn"`, `"syn,ack"`, `"ack,bak"` messages.

---

### Q8: Create a script that tests whether a remote server allows telnet access (port 23).

**Answer:**

* Implemented in **ans_8.py**.

```python
import socket

def test_port(address: str, dest_port: int) -> bool:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            print("waiting for connection")
            if sock.connect_ex((address, dest_port)) == 0:
                print("connected")
                return True
        return False
    except (OSError, ValueError) as e:
        print(f"⚠️ Error: {e}")
        return False
    
def main():
    address = "64.233.160.0"
    port = 23

    if test_port(address=address , dest_port=port):
        print("connection")
    else:
        print("no connection")

if __name__ == "__main__":
    main()
```

---

### Q9: Write a UDP client that sends a DNS request manually to 8.8.8.8.

**Answer:**

* Implemented in **ans_9.py** (reverse DNS lookup).

```python
import socket

ip = '8.8.8.8'
hostname = socket.gethostbyaddr(ip)
print(f"Host name for IP {ip}: {hostname[0]}")
```

---

### Q10: Implement a simple packet sniffer that captures TCP and UDP packets.

**Answer:**

* Implemented in **ans_10.py** using Scapy.

```python
from scapy.all import sniff

def show_packet(packet):
    print(packet.summary())

print("Sniffing packets... press Ctrl+C to stop.")
sniff(prn=show_packet, count=0)
```
