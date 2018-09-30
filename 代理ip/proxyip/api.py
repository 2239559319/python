import random

def getip():
    iplist=[]
    with open("ip.txt") as f:
        iplist=f.readlines()
    r=random.randint(1,len(iplist)-1)
    return iplist[r]

print(getip())