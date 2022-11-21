import socket
client=socket.socket()
# connecting with local host ip address on port 5050
client.connect(('localhost',4376))
# for exiting of program
check=True
while(check==True):
    msg=client.recv(1024)
    # decoding the message
    msg.decode('utf-8')
    # printing message
    print(msg)
    # closing the connection
    client.close()
    check=False