import socket

target_host = "127.0.0.1"
target_port = 22334

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
client.sendto("AABBCC", (target_host,target_port))