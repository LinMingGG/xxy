
import requests
import json
import time 
import os

# 配置开始
user = os.environ["USER"]
account = user.split( )[0] # 账号
password = user.split( )[1] # 密码
school_id = user.split( )[2] # 学校ID
sign_gps = os.environ["SIGN_GPS"]  # 签到坐标（注意小数点取后6位）
longitude1 = sign_gps.split(",")[0] # 经度
latitude1 = sign_gps.split(",")[1] # 纬度
SCKEY=os.environ["SCKEY"]
address = os.environ["ADDRESS_NAME"]
address_detail = os.environ["ADDRESS_DETAIL"]
   
data={'account':account,#账号
      'app_id':'cn.vanber.xixunyun.saas',
      'app_version':'4.9.9',
      'key':'',
      'model':'huawei tag-tl00',
      'password':password,#密码
      'platform':'2',
      'registration_id':'1a0018970a242ca8039',
      'request_source':'3',
      'school_id':school_id,#学校代码
      'system':'5.1.1',
      'uuid':'00:81:24:d9:fc:da'}
login_header={
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '227',
        'Host': 'api.xixunyun.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.8.1',

}
login_url=' https://api.xixunyun.com//login/api?from=app&version=4.9.9&platform=android&entrance_year=0&graduate_year=0'
request=requests.post(url=login_url,headers=login_header,data=data)
login_data=json.loads(request.text)#登陆成功后返回的信息
token=login_data['data']['token']
time.sleep(1)

longitude=longitude1
latitude=latitude1
print(login_data)
sign_url='https://api.xixunyun.com/signin_rsa?token='+token+'&from=app&version=4.1.5&platform=android&entrance_year=0&graduate_year=0 '
sign_data={'address':address_detail,#签到地址
           'address_name':address,#签到地点名称
           'change_sign_resource':'0',
           'comment':'',
           'latitude':"PcsiE2OsHB5/8tdtamFezKcg9jYp4lKOryX8mG68mE32nVFwh1BNzaJgDIaUK0QOnz7iGDgOcyGMwbB85zJT7wf3Dczy5O9z3/mTBOH9zOFhxKhUSUqlpKdfG5+ZV8UJF6evTcYci5YPIpqGI6uifnQmyB/X86bcNGqe1f2i0WU=",
           'longitude':"fS0dMPGfCMjpBmLZgJKV6GXjlC/PD8ZaVlsxSsXopLOPkctgbRuNfGThWBXdjuOY0ESvvWg+l6oYrhMsiHvrTrpJKyy95bMhDW83SNbLrvHQcvdlo5I+ApSYTBNRxvRHqDlSOifwRUdweCBKgrSs26YLP0JWZPwAK54uwNruN3U=",
           'remark':'1',
    
    }
sign_request=requests.post(url=sign_url,data=sign_data,headers=login_header)
sign=json.loads(sign_request.text)
print(sign)

                                     

if len(SCKEY) >= 1:
  url = 'https://sc.ftqq.com/'+SCKEY+'.send'
  requests.post(url, data={"text": "习讯云签到提醒", "desp": sign_request.text})
os.system("pause")

print(longitude)
print(latitude)



import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
fromaddrs = '\u0031\u0038\u0033\u0030\u0036\u0030\u0039\u0032\u0035\u0032\u0033\u0040\u0031\u0036\u0033\u002e\u0063\u006f\u006d'
password2 = '\u0045\u0059\u0049\u0050\u0042\u004e\u0056\u004f\u0054\u004b\u0045\u004b\u0050\u0059\u0042\u0053'  
toaddrs = os.environ["EMAIL"]
def mail():
    ret = True
    try:
        msg = MIMEText(sign_request.text, 'plain', 'utf-8')
        msg['From'] = formataddr(["习讯云签到提醒", fromaddrs])  # 发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["习讯云自动签到程序", toaddrs])  # 收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "习讯云自动签到提醒"  # 邮件的主题

        server = smtplib.SMTP_SSL("smtp.163.com",)  # qq邮箱SMTP服务器，端口是25
        server.login(fromaddrs, password2)  # 发件人邮箱账号、邮箱密码
        server.sendmail(fromaddrs, [toaddrs, ], msg.as_string())  # 发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret
ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")

