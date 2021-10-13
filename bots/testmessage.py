import smtplib
from email.mime.text import MIMEText
from email.header import Header

host = "smtp.qq.com"
mail_pass = "iaqfotkwamjhcaig"
sender = '85157355@qq.com'
receiver = '85157355@qq.com'
content = 'hello~'
message = MIMEText(content, 'plain', 'utf-8')
message['From'] = Header("Lao Gao", 'utf-8')
message['To'] = Header("Hai shi Lao Gao", 'utf-8')
subject = 'testing message'
message['Subject'] = Header(subject, "utf-8")
smtpObj = smtplib.SMTP_SSL(host, 465)
smtpObj.login(sender, mail_pass)
smtpObj.sendmail(sender, receiver, message.as_string())
smtpObj.quit()
print('done')
