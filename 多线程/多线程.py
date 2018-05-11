#encoding=utf-8
import threading

class mythread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name

    def run(self):
        print self.name

t1=mythread('wan')
t2=mythread('chuan')
t1.start()
t2.start()