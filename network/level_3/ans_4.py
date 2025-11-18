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