from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

#mutipart alternative:text and html
def make_mpa_msg():
    email=MIMEMultipart('alternative')
    text=MIMEText('Hello World!\r\n','plain')
    email.attach(text)
    html=MIMEText(
        '<html><body><h4>Hello World!</h4>'
        '</body></html>','html'
    )
    email.attach(html)
    return email

#mutiternative:images
def make_img_msg(fn):
    f=open(fn,'r')
    data=f.read()
    f.close()
    email=MIMEImage(data,name=fn)
    email.add_header('Connect-Disposition','attachment;filename="%s"'%fn)
    return email

def sendMsg(fr,to,msg):
    s=SMTP('localhost')
    errs=s.sendmail(fr,to,msg)
    s.quit()

if __name__=="__name__":
    print("Sending mutipart alternative msg...")
    msg=make_mpa_msg()
    msg['From']=SENDER
    msg['To']=', '.join(RECIPS)
    msg['Subject']='mutipart alternative test'
    sendMsg(SENDER,RECIPS,msg.as_string())

    print("sending image msg...")
    msg=make_img_msg(SOM_IMG_FILE)
    msg['From']=SENDER
    msg['To']=', '.join(RECIPS)
    msg['Subject']='img file test'
    sendMsg(SENDER,RECIPS,msg.as_string())