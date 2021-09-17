# ##习讯云自动签到##
<code>2021年3月13日 18:00更新</code><br>

为了让同学们更加认真、更加专注听课，而不去用手机签到花费大量时间、耗费大量精力，请自行合理使用！请点击下方View all of README.md了解更多。

本项目支持习讯云的签到，可以自定义位置。

本脚本最大的不同应该就是基于github action运行，所以并不需要服务器、不需要服务器、不需要服务器同样也不需要掌握任何python的相关设置，你所需要准备的就是一个github账号以及一个耐而不烦的心。傻瓜式的操作却可以解决你最大的痛苦。

### 特点
1、本项目支持任何形式的习讯云签到。
2、基于server酱使得签到成功时会将签到信息发送至你的微信。
2、无需挂在任何服务器上，只需要点几下，让github自动为你签到。
3、使用强大的GitHub actions功能，实现无服务器实时监控您的习讯云签到。
4、无需掌握任何编程知识，强大的后端后端已做好，您仅需点击几下。

自动签到时间：上午8点 下午14点 
如果签到异常，请在代码第54行处修改0为1

### 1、配置参数
在Setting里的secrets添加参数如下：

name: <code>USER</code><br>
value: <code>账号 密码 学校代码</code><br>  （用空格或回车分开，学校代码 可以前往 https://api.xixunyun.com/login/schoolmap 查询 如渝水职院：1743）

name: <code>SIGN_GPS</code><br>
value: 你的地理位置坐标经纬度 如<code>105.931252,29.367364</code><br>   (获取地址坐标位置： https://lbs.amap.com/console/show/picker 高德取坐标)

name: <code>ADDRESS_NAME</code><br>
value: <code>地址名称</code><br>    此添加为选用 可忽略

name: <code>EMAIL</code><br>
value: <code>你的邮箱地址</code><br>     (用于接收签到提醒  Code=20000 表示签到成功)此添加为选用

name: <code>SCKEY</code><br>
value: <code>Server酱接口号</code><br>  (用于微信Server酱接收签到提醒 如<code>SCU95156T515985ffca658bf1b801c24983lm77215ea134d3265nm</code><br>)  此添加为选用

### 2、启动程序
设置好环境变量后点击你的仓库上方的 Actions 选项，会打开一个如下的页面，点击 I understand... 按钮确认在 Fork 的仓库上启用 GitHub Actions 。

最后在你这个 Fork 的仓库内随便改点什么（比如给 README 文件删掉或者增加几个字符）提交一下手动触发一次 GitHub Actions 就可以了 （重要！！！测试发现在 Fork 的仓库上 GitHub Actions 的定时任务不会自动执行，必须要手动触发一次后才能正常工作） 。

### 其他项目链接请访问：<code>http://1.15.229.3/</code><br> 
