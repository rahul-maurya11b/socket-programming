
import socket
# creating socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())
# connecting the client
client.connect((ip,8899))
print("client conected")


# read binary data from image file
file=open('received.txt','wb')

# receiving the data
msg=client.recv(1024)
while msg:

    file.write(msg)
    msg=client.recv(1024)
file.close()
check=open('received.txt','r')
data=check.read()
print(data)

# making the text in list form 