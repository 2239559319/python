from socket import *

host='localhost'
port=21567
bufsiz=1024
addr=(host,port)

udpCliSock=socket(AF_INET,SOCK_DGRAM)

while True:
    data=raw_input('> ')
    if not data:
        break
    udpCliSock.sendto(data,addr)
    data,addr=udpCliSock.recvfrom(bufsiz)
    if not data:
        break
    print data

udpCliSock.close()