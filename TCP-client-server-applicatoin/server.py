
import socket,sys
# creating socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())
print("Server is running")
server.bind((ip,8899))
server.listen(4)

# accepting the client request
client,address=server.accept()

print("Server is ready to accept data ...")
print("connected with client having",address)


file=open(sys.argv[1],'rb')
file_data=file.read()
while file_data:
    client.send(file_data)
    file_data=file.read()

client.close()
file.close()


        
