#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request, parse
import json
import base64
import re
import os
import shutil
import getpass
import sys
import time


def connect_network():
    url = 'http://10.255.255.13/index.php/index/login'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    referer = 'http://10.255.255.13'
    origin = 'http://10.255.255.13'
    username = input('Enter your username(Student number or mobile number):\n')
    domain = input('Enter your domain(ChinaNet/Unicom/CMCC/NUIST):\n')
    password = base64.b64encode(str.encode(
        getpass.getpass('Enter your password:\n')))
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
    return username, domain, password


def change_config(username, domain, password, query):
    shutil.copy2(os.getcwd()+'/auto_inuist.py', os.getcwd()+'/'+query+'.py')
    old = os.getcwd()+'/auto_inuist.py'
    new = os.getcwd()+'/'+query+'.py'
    o = open(old, mode='r')
    n = open(new, mode='w')
    for line in o:
        n.write(line.replace('username = input(\'Enter your username(Student number or mobile number):\\n\')', 'username = \''+username+'\'')
                .replace('domain = input(\'Enter your domain(ChinaNet/Unicom/CMCC/NUIST):\\n\')', 'domain = \''+domain+'\'')
                .replace('password = base64.b64encode(str.encode(getpass.getpass(\'Enter your password:\\n\')))', 'password = '+str(password)))
    o.close()
    n.close()


sys.argv[0]
username, domain, password = connect_network()
if len(sys.argv) < 2:
    ticks = time.strftime('time_%Y%m%d%H%M%S', time.localtime(time.time()))
    change_config(username, domain, password, ticks)
else:
    change_config(username, domain, password, sys.argv[1])
