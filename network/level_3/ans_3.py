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
