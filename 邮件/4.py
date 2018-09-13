import smtplib
from email.message import EmailMessage

msg=EmailMessage()
msg.set_content("测试邮件")

sender="w773127754@163.com"
password="w2239559319"
receiver="2239559319@qq.com"

msg["Subject"]="这是测试邮件邮件头"
msg["From"]=sender
msg["To"]=receiver

s=smtplib.SMTP("smtp.163.com",25)
s.login(sender,password)
s.send_message(msg)
print("发送成功")
s.quit()

'''
msg["From"]和msg["To"]中如果有非ascii字符的话要用Header()
'''