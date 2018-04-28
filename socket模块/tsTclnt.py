from socket import *

host='localhost'
port=21567
bufsiz=1024
addr=(host,port)

tcpCliSock=socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(addr)

while True:
    data=raw_input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    data=tcpCliSock.recv(bufsiz)
    if not data:
        break
    print data

tcpCliSock.close()