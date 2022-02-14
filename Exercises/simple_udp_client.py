import socket

target_host = "172.16.1.14"
target_port = 22334

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
client.sendto("AABBCC", (target_host,target_port))