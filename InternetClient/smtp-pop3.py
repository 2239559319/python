#encoding=utf-8
from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSVR="smtp.python.is.cool"  #发送服务器
POP3SVR="pop.python.is.cool"   #接受邮件服务器

who="wesley@python.is.cool"
body='''\
From:%(who)s
To:%(who)s
Subject:test msg

Hello World!
'''%{"who":who}
#发送
sendSvr=SMTP(SMTPSVR)
errs=sendSvr.sendmail(who,[who],body)
sendSvr.quit()
assert len(errs)==0,errs
sleep(10)#wait for mail to be delivered

recvSvr=POP3(POP3SVR)
recvSvr.user("weslry")
recvSvr.pass_("youllneverguess")
rsp,msg,siz=recvSvr.retr(recvSvr.stat()[0])
#strip headers and compare to orig msg
sep=msg.index('')
recvBody=msg[sep+1:]