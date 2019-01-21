#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib
import request, parse
import json
import base64
import re
import os
import shutil
import platform
import getpass
def pingtest(IP):
    if platform.system() == 'Windows':
        net = os.popen('ping ' + IP + ' -n 1 | find /i "100" /c')
    else:
        net = os.popen('ping ' + IP + ' -c 1 | grep "100" | wc -l')  
    ping = net.read()
    return ping
def connect_network():
    url = 'http://10.255.255.13/index.php/index/login'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    referer = 'http://10.255.255.13'
    origin = 'http://10.255.255.13'
    username = input('Enter your username(Student number or mobile number):\n')
    domain = input('Enter your domain(ChinaNet/Unicom/CMCC/NUIST):\n')
    password = base64.b64encode(str.encode(getpass.getpass('Enter your password:\n')))
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
    return username,domain,password
def scheduled_task():    
    if platform.system() == 'Windows':
        print('Please use the scheduled task to set up automatic login. You need to add auto_nuist.py to the scheduled task.')
    else:
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
                print('If you fail to create a scheduled task, run \'crontab -e\' and enter \'7-23/10 * * * * python3 '+old+'\\auto_nuist.py\', then run \'sudo /usr/sbin/cron restart\' to enabling it!')
def change_config(username,domain,password,scheduled_task_need):
    shutil.copy2(os.getcwd()+'/auto_inuist.py',os.getcwd()+'/auto_inuist_tmp.py')
    old = os.getcwd()+'/auto_inuist.py'
    new = os.getcwd()+'/auto_inuist_tmp.py'
    o = open(old, mode='r')
    n = open(new, mode='w')
    for line in o:
        n.write(line.replace('username = input(\'Enter your username(Student number or mobile number):\\n\')', 'username = \''+username+'\'')\
        .replace('domain = input(\'Enter your domain(ChinaNet/Unicom/CMCC/NUIST):\\n\')', 'domain = \''+domain+'\'')\
        .replace('password = base64.b64encode(str.encode(getpass.getpass(\'Enter your password:\\n\')))', 'password = \''+password.decode()+'\'')\
        .replace('scheduled_task_need = 1','scheduled_task_need = '+str(scheduled_task_need)))
        .replace('use_time = 1','use_time = 0'))
    o.close()
    n.close()
    os.remove(old)
    os.rename(new, old)
print('Network connection testing...')
pingtest_local = pingtest('127.0.0.1')
if pingtest('114.114.114.114') != pingtest_local:
    print('Unable to access the internet, trying to connect...')
    if pingtest('10.255.255.13') != pingtest_local:
        print('The authentication server is unavailable. Please check the network status.')
    else:
        print('Authentication server is available, login...')
        scheduled_task_need = 1
        use_time = 1
        username,domain,password = connect_network()
        if use_time
            change_config(username,domain,password,1)
        print('Login is complete! Retest network connections...')
        if pingtest('114.114.114.114') != pingtest_local:
            print('No network connection, please check the account status!')
        else:
            print('Network connection completed!')
        if scheduled_task_need:
            if input('Do you need to use scheduled tasks for automatic login now?(Y/N)\n') == "Y":
                scheduled_task()
                change_config(username,domain,password,0) 
            else:
                if input('Do you always refuse to use program certification?(Y/N)\nEnter Y to deny the use of the scheduled task, otherwise you will be asked if you want to use the scheduled task each time you manually run the script until you automatically use the scheduled task.\n') == "Y":
                    change_config(username,domain,password,0) 
else:
    print('The network status is normal and no authentication is required.')