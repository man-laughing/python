#!/usr/bin/env python

import smtplib

mail_host = 'smtp.qq.com'
mail_port = '465'

send_user = '305835227@qq.com'
send_pass = 'xxxxxx'

rece_user = '18807522651@163.com'
content = '''
   hello:
      My name is zhanglei,How are you ?
'''


def run():
    smtp = smtplib.SMTP_SSL()
    smtp.connect(mail_host,mail_port)
    smtp.login(send_user,send_pass)
    smtp.sendmail(send_user,rece_user,content)
    smtp.close()

if __name__ == "__main__":
    run()
