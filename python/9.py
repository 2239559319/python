import time
import datetime

def intervel(func,rightTime):
    '''
    循环直到条件为True
    : params: func要执行的函数
    : rightTime: 到达的时间（到了这个时间点执行函数）
    :return:
    '''
    while(True):
        if isRightTime(rightTime):
            func()
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
def p():
    print('Hello World')
intervel(p,21)