import socket


ip = '8.8.8.8'
hostname = socket.gethostbyaddr(ip)
print(f"Host name for IP {ip}: {hostname[0]}")