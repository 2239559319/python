from SocketServer import (TCPServer as TCP,
      StreamRequestHandler as SRH)
from time import ctime

host=''
port=21567
addr=(host,port)

class MyRequestHandler(SRH):
    def handle(self):
        print '...connected from:',self.client_address
        self.wfile.write('[%s] %s' %(ctime(),self.rfile.readline()))

tcpServ=TCP(addr,MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()