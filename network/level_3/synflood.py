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
    while True:
        a =0 
    return
    

def start():
    answer = int(input("enter the number of clients for the attack: "))
    for i in range(answer):
        thread = threading.Thread(target=client)
        thread.start()

if __name__ == "__main__":
    start()