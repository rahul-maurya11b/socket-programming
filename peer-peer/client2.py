import socket,sys,threading

ip='localhost'
rahul=(ip,55555)

print('connecting to rahul server')

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.bind(('localhost',50001))
client.sendto(b'0',rahul)

while True:
    data=client.recv(1024).decode()

    if data.strip()=='ready':
        print('checked in with server,waiting')
        break

data=client.recv(1024).decode()
ip,sport,dport=data.split(" ")
test=data.split(" ")
sport=int(sport)
dport=int(sport)
print('got peer')
print(test)
