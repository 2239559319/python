import random
import os

os.chdir("proxyip")
def getip():
    iplist=[]
    with open("ip.txt") as f:
        iplist=f.readlines()
    r=random.randint(1,len(iplist)-1)
    return iplist[r].strip()