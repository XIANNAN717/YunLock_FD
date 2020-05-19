from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
import os


def send_report(file_new):
    with open(file_new,"rb") as f:
        mail_body = f.read()

    # qq邮箱服务器
    host_server = "smtp.qq.com"

    # 发件人登录qq邮箱的账号
    sender_qq = "596609597@qq.com"

    # qq邮箱授权码（不是密码）
    pwd = "tnquocjbpndobfec"

    # 发件人的邮箱地址
    sender_qq_mail = "596609597@qq.com"

    # 收件人的邮箱邮箱地址
    receiver = "596609597@qq.com"

    # 邮件标题
    mail_tilte = "自动化测试报告"

    msg = MIMEMultipart()
    msg["Subject"] = Header(mail_tilte,"utf-8")
    msg["From"] = sender_qq_mail

    # 邮件正文内容
    msg.attach(MIMEText(mail_body,"html","utf-8"))

    # SSL登录
    smtp = SMTP_SSL(host_server)

    smtp.ehlo(host_server)
    smtp.login(sender_qq,pwd)

    smtp.sendmail(sender_qq_mail,receiver,msg.as_string())

    smtp.quit()

    print("Test report has send out!!")


# 查找测试报告，找出最新的测试报告
def new_report(testReport):
    lists = os.listdir(testReport)
    newLists = sorted(lists)
    file_new = os.path.join(testReport,newLists[-1])

    return file_new

from config import global_config
report_path = global_config.report_path
print(report_path)

if __name__ == '__main__':
    new_report = new_report(report_path)
    print(new_report)
    send_report(new_report)




