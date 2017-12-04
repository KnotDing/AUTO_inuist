This is a python3 project for students of NUIST who use i-nuist.
You can use it on your linux, windows, openwrt or other unix.


----------

**auto_inuist.py**

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request, parse
import json

url = 'http://10.255.255.13/index.php/index/login'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
referer = 'http://10.255.255.13'
origin = 'http://10.255.255.13'

username = '账号' #手机号或学号
domain = '运营商' #选填ChinaNet\Unicom\CMCC\NUIST
password = '密码' #加密后的密码，非明文密码，可用chrome抓包
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
```

Auto_inuist.py is a python3 script which is under the disguise of browser for authentication.

----------

**net_test.sh**

```sh
PING=`ping -c 3 114.114.114.114 | grep '64 bytes' | wc -l`
NOT_PING="0"
if [ "$PING" -eq "$NOT_PING" ]
then
  python3 /etc/auto_inuist.py    #python脚本目录
fi
```

Net_test.sh is a sh script which is used for testing network.If there are not a available connection, it will run auto_inuist.py.


----------

**root**

    */1 * * * * sh /etc/net_test.sh

Root is a file for crontab. It is just a example.You should use `crontab -e` to creat a task to run net_test.

## Have fun!
