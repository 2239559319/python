import gevent

list=[]
def run(num):
    print("coroutine%d is running"%num)
if __name__=="__main__":
    for i in range(1,6):
        gevent.joinall(run(i))