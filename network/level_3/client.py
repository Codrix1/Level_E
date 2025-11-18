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
