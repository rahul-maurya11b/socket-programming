import socket


msg  ="Hello UDP hero"
msg=bytes(msg.encode())
serverAddressPort  = ("localhost", 20003)
# Create a UDP socket at client side
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Send to server using created UDP socket
client.sendto(msg,serverAddressPort)
msgFromServer = client.recvfrom(1024)
print(f"server {msgFromServer[1][0]} has message {msgFromServer[0]}")