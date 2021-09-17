# ##习讯云自动签到##
2021年3月13日 18:00

自动签到时间：上午8点 下午14点
如果签到异常，请在代码第54行处修改0为1
1
在Setting里的secrets添加参数如下：

name: USER
value: 账号 密码 学校代码    1911170164 By456789 1743（用空格或回车分开）

name: SIGN_GPS
value: 你的地理位置坐标经纬度 如105.931252,29.367364

name: ADDRESS_NAME
value: 地址名称    此添加为选用 可忽略

name: EMAIL
value: 你的邮箱地址     (用于接收签到提醒  Code=20000 表示签到成功)此添加为选用

name: SCKEY
value: Server酱接口号  (用于微信Server酱接收签到提醒 如SCU95156T515985ffca658bf1b801c24983lm77215ea134d3265nm )此添加为选用



