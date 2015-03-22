# 这个项目就是写了一个自动登录canglaoshi.mobi并且实现自动签到以获取流量的小脚本，其他的没啥了
1024.canglaoshi.mobi自动登录签到器

仅限于该网站的自动登录，该网站提供shadowsocks账户，并且根据规则每天签到会自动获取1G的流量，该脚本用于自动登录并且自动签到，并将签到获取的流量结果存放在与该脚本同目录下的“日期_shadowsocks.txt”文档中

该脚本在Mac OSX系统下编写和测试，对于其他的系统没有做过测试

作者使用Crontab来执行定时任务，Crontab命令如下：

```shell

	1 0 * * * /usr/bin/python /Users/EricTang/Documents/EricTangOwnProject/PythonWorkspace/ShadowsocksFlowRateAutoGet/autologin.py
```

同时，理论上也可以使用Mac系统自带的LaunchAgents来执行定时任务，或者在windows系统下使用计划任务来完成。
