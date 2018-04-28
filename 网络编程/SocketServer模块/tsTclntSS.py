from socket import *

host='localhost'
port=21567
bufsiz=1024
addr=(host,port)

while True:
    tcpCliSock=socket(AF_INET,SOCK_STREAM)
    tcpCliSock.connect(addr)
    data=raw_input('> ')
    if not data:
        break
    tcpCliSock.send('%s\r\n'%data)
    data=tcpCliSock.recv(bufsiz)
    if not data:
        break
    print data.strip()
    tcpCliSock.close()