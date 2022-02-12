import socket

localIP = "0.0.0.0"
localPort = 22334

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and IP
UDPServerSocket.bind((localIP, localPort))
print "UDP Server up and listening"

# Listen for incoming datagrams
while(True):
    data, addr = UDPServerSocket.recvfrom(1024)
    print data