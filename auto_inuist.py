#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request, parse
import json
import base64

url = 'http://10.255.255.13/index.php/index/login'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
referer = 'http://10.255.255.13'
origin = 'http://10.255.255.13'

username = '账号'#手机号或学号
domain = '运营商'#选填ChinaNet\Unicom\CMCC\NUIST
password = base64.b64encode('密码')#密码
enablemacauth = '0'
login_data = parse.urlencode([
    ('username', username),
    ('password', password),
    ('domain', domain),
    ('enablemacauth', enablemacauth)
])
req = request.Request(url)
req.add_header('Origin', origin)
req.add_header('User-Agent', user_agent)
req.add_header('Referer', referer)
with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)

