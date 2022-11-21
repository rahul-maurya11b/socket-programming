import socket

# object of server
server=socket.socket()
# bind ip with this port
server.bind(('localhost',4376))
# can listen max upto 4 devices
server.listen(4)
# accepting client
client,address=server.accept()

print("server is ready to accept ....")
print("connected with client ",address[0])
check=True
while (check==True):
# 1024 =size
    msg=input("enter message..")
    # encoding message
    client.send(msg.encode('utf-8'))
    server.close()
    check=False