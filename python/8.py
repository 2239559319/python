import time
import datetime

def intervel():
    '''
    循环直到条件为True
    :return:
    '''
    while(True):
        if isRightTime(26):
            #dosomethings
            print("到时间了")
            break
        else:
            time.sleep(1)
        print(datetime.datetime.now().time())

def isRightTime(rightTime):
    '''
    判断是否到了确定时间
    :param rightTime: 确定的时间
    :return:
    '''
    date=datetime.datetime.now()
    if date.minute==rightTime:                 #在某时40分的时候返回true
        return True
    else:
        return False

intervel()