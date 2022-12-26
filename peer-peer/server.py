import socket
port=50002
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("0.0.0.0",55555))

while True:
    clients=[]
    while True:
        data,address=server.recvfrom(128)
        print('connection from: {}'.format(address))
        clients.append(address)
        server.sendto(b'ready',address)
        
        if len(clients) ==2:
            print("got 2 client, sending details to each")
            break
    c1=clients.pop()
    c1_address,c1_port=c1
    c2=clients.pop()
    c2_address,c2_port=c2

    server.sendto("{} {} {}".format(c1_address,c1_port,port).encode(),c2)
    server.sendto("{} {} {}".format(c2_address,c2_port,port).encode(),c1)
