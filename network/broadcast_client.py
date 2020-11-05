import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) 

# Enable broadcasting mode
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

client.bind(("", 37020))
while True:
    # Thanks @seym45 for a fix
    data, addr = client.recvfrom(1024)
    print("received message: %s"%data)
