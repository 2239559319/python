import smtplib
from email.mime.text import MIMEText

sender="306234087@qq.com"
password="fgdbsnksjtwhbhji"
receiver="w2239559319@outlook.com"

subject = "python发邮件测试"
content = "这是我使用python smtplib模块和email模块自动发送的邮件"

msg=MIMEText(content,"plain","utf-8")
msg['Subject'] = subject
msg['From'] = sender
msg['TO'] = receiver
try:
    s = smtplib.SMTP_SSL('smtp.qq.com',465)
    s.login(sender,password)
    s.sendmail(sender,receiver,msg.as_string())
    print("发送成功")
except Exception:
    print("发送失败")