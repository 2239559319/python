import smtplib
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

sender="306234087@qq.com"
password="fgdbsnksjtwhbhji"
receiver="2017141461249@stu.scu.edu.cn"

subject="python发送带有图片的邮件"
msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = receiver

msg.attach(MIMEText('使用python smtplib模块和email模块自动发送邮件测试','plain','utf-8'))
img_file = open(os.getcwd()+"/1.jpg",'rb').read()       #getcwd()函数返回当前工作目录
msg_img = MIMEImage(img_file)
msg_img.add_header('Content-Disposition','attachment', filename = "1.jpg")
msg_img.add_header('Content-ID', '<0>')
msg.attach(msg_img)

s = smtplib.SMTP_SSL('smtp.qq.com',465)
s.set_debuglevel(1)
s.login(sender,password)
s.sendmail(sender,receiver,msg.as_string())
s.quit()