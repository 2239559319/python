#此模块是筛选模块
import getip
import requests
import threading
import os

mylock=threading.RLock()
class filter(threading.Thread):

    def __init__(self,name,list):
        threading.Thread.__init__(self)
        self.name=name
        self.list=list

    def run(self):
        url = "http://2018.ip138.com/ic.asp"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        }
        for i in self.list:
            print("%s在进行第%d次筛选"%(self.name,self.list.index(i)+1))
            proxies = {
                "http":i
            }
            try:
                r = requests.get(url=url, headers=headers, proxies=proxies, timeout=2)
                r.encoding = "gbk"
                if "您的IP地址" in r.text:
                    mylock.acquire()
                    with open("ip.txt","a") as f:
                        f.write(i+"\n")
                    mylock.release()
            except Exception:
                continue
        print("%s已完成"%self.name)

def updateip():
    '''
    更新ip文件
    :return: True更新完成，可以读取ip.txt
    '''
    if(os.path.exists("ip.txt")):
        os.remove("ip.txt")
        thread1 = filter("西刺代理", getip.getxiciip(1))
        thread2 = filter("快代理", getip.getkuaidailiip(2))
        thread3 = filter("89代理", getip.get98mianfeiip(2))
        thread4 = filter("5u代理",getip.get5uip())
        thread5 = filter("米扑代理", getip.getmipuip())
        thread6=filter("y代理",getip.getyqieip())
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread5.start()
        thread6.start()
        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()
        thread5.join()
        thread6.join()
    else:
        thread1 = filter("西刺代理", getip.getxiciip(1))
        thread2 = filter("快代理", getip.getkuaidailiip(2))
        thread3 = filter("89代理", getip.get98mianfeiip(2))
        thread4 = filter("5u代理", getip.get5uip())
        thread5 = filter("米扑代理", getip.getmipuip())
        thread6 = filter("y代理", getip.getyqieip())
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread5.start()
        thread6.start()
        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()
        thread5.join()
        thread6.join()