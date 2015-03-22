#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author	:	EricTang
#Date	:	2015年03月11日09:14:54
#Desc	:	用来自动登录1024.canglaoshi.mobi并且自动签到以获取Shadowsocks流量
#
import requests
import re
import datetime

login_url = "https://1024.canglaoshi.mobi/user/dologin.php"
check_url = "https://1024.canglaoshi.mobi/user/docheckin.php"
header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36' }

EricTang_Accounts = {
		1 : {
			"username" : "账户1", 
			"password" : "密码1"
		},
		2 : {
			"username" : "账户2", 
			"password" : "密码2"
		},
		3 : {
			"username" : "账户3", 
			"password" : "密码3"
		},
		4 : {
			"username" : "账户4", 
			"password" : "密码4"
		},
	}

def autoLogin(username, password):
	"""
	自动登录
	"""
	form_data = {
		"username" : username,
		"password" : password,
	}
	s = requests.session()
	# 发起网络请求
	login_response = s.post(login_url, data = form_data, headers = header)
	login_res_content = login_response.content
	# print(login_res_content)
	if login_res_content.find("用户名或密码错误") != -1:
		writeResult("登录【" + username + "】时，用户名或者密码错误，请手动检查一下")
	elif login_res_content.find("docheckin") != -1:
		check_response = s.post(check_url, data = None, headers = header)
		check_res_content = check_response.content
		# print check_res_content
		# 签到成功的话，获取一下该账号今日获得的流量
		match_content = re.search("(签到成功.*流量).*", check_res_content)
		# 保存结果
		checkin_result_str = "账户【" + username + "】" + match_content.group(1)
		writeResult(checkin_result_str)
	elif login_res_content.find("不能签到") != -1:
		writeResult("账户【" + username + "】已经签过到了")
#end def

def writeResult(content):
	"""
	将签到结果保存到txt文档中
	"""
	# 想了想还是保存到txt文本里，方便我自己查看的比较好
	today_date = datetime.date.today()
	result = open(str(today_date) + "_shadowsocks.txt", "a")
	result.write(content + "\n")
	result.close()
#end def
if __name__ == "__main__":
	"""
	主方法
	"""
	for i in xrange(1,len(EricTang_Accounts)+1):
		autoLogin(EricTang_Accounts[i]["username"], EricTang_Accounts[i]["password"])