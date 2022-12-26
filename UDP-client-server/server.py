import socket

localhost = "127.0.0.1"
Port = 20001
msg = "Hello UDP Client"
# Create a datagram socket
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# Bind to address and ip
server.bind((localhost, Port))
print("UDP server up and listening")
# Listen for incoming datagrams
while(True):
    data = server.recvfrom(1024)
    message =data[0]
    address = data[1]
    print(f"client{address} has message{message }")
    # Sending a reply to client
    server.sendto(bytes((msg).encode()), address)
