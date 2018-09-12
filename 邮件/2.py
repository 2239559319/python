import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender="306234087@qq.com"
password="fgdbsnksjtwhbhji"
receiver="w2239559319@outlook.com"

subject="python发送html邮件测试"
content="""
<p>python 邮件发送测试</p>
<p><a href="http://www.baidu.com">这是一个链接</a></p>
"""
msg=MIMEText(content,"html","utf-8")
msg["Subject"]=Header(subject,"utf-8")
msg["From"]=Header("大傻子","utf-8")
msg["To"]=Header("二愣子","utf-8")

s=smtplib.SMTP_SSL("smtp.qq.com",465)
s.login(sender,password)
s.sendmail(sender,receiver,msg.as_string())
print("发送成功")
s.quit()