#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request, parse
import json
import base64
import re
import os
import shutil
import platform

if platform.system() == 'Windows':
    net = os.popen('ping 114.114.114.114 | find /i "100" /c')
else:
    net = os.popen('ping -c 3 114.114.114.114 | grep "100" | wc -l')  
ping = net.read()
if ping != '0\n':
    url = 'http://10.255.255.13/index.php/index/login'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    referer = 'http://10.255.255.13'
    origin = 'http://10.255.255.13'
    first_use = 1
    username = input('Enter your username(Student number or mobile number):\n')
    domain = input('Enter your domain(ChinaNet/Unicom/CMCC/NUIST):\n')
    password = base64.b64encode(str.encode(input('Enter your password:\n')))
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
    if first_use:
        shutil.copy2(os.getcwd()+'/auto_inuist.py',os.getcwd()+'/auto_inuist_tmp.py')
        old = os.getcwd()+'/auto_inuist.py'
        new = os.getcwd()+'/auto_inuist_tmp.py'
        o = open(old, mode='r')
        n = open(new, mode='w')
        for line in o:
            n.write(line.replace('username = input(\'Enter your username(Student number or mobile number):\\n\')', 'username = \''+username+'\'')\
            .replace('domain = input(\'Enter your domain(ChinaNet/Unicom/CMCC/NUIST):\\n\')', 'domain = \''+domain+'\'')\
            .replace('password = base64.b64encode(str.encode(input(\'Enter your password:\\n\')))', 'password = \''+password.decode()+'\'')\
            .replace('first_use = 1', 'first_use = 0'))
        o.close()
        n.close()
        os.remove(old)
        os.rename(new, old)
        if platform.system() == 'Windows':
            print('Please use the scheduled task to set up automatic login. You need to add auto_nuist.py to the scheduled task.')
        else:
            if input('Do you need to use scheduled tasks for automatic login?(Y/N)') == "Y":
                crontab = os.getcwd()+'/crontab'
                if not os.path.exists(crontab):
                    c = open(crontab,'w')
                    c.write('7-23/10 * * * * python3 '+old+'\n')
                    c.close()
                    os.system('crontab ./crontab')
                    if platform.system() == 'Linux':
                        os.system('service cron restart')
                    else:
                        os.system('sudo /usr/sbin/cron restart')
                        print('If you fail to create a scheduled task, run \'crontab -e\' and enter \'7-23/10 * * * * python3 '+old\
                        +'\\auto_nuist.py\', then run \'sudo /usr/sbin/cron restart\' to enabling it!')
