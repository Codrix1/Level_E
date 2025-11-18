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
