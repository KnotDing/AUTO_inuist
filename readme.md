This is a python3 project for students of NUIST who use i-nuist.
You can use it on your linux, windows, openwrt or other unix.


----------

**auto_inuist.py**

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

