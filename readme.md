# Hello

This is a python3 project for students of NUIST who use i-nuist.
You can use it on your linux, windows, openwrt or other unix.

---------

## auto_inuist.py

Auto_inuist.py is a python3 script which is under the disguise of browser for authentication.
You need to enter your account number, password and operator information for first use.
You can use `python3 auto_inuist.py 'name'` to creat a file with confirmation, and use `python3 auto_inuist_easy.py 'name'` to creat a file without confirmation. The new file will be named as 'name'. If you don't enter 'name', the current time will be used to create the file.
In the future, you can use `python3 'name'.py` or `python3 'time'.py`for authentication without entering the account number, password and operator information.

---------

## net_test.sh

~~Net_test.sh is a sh script which is used for testing network. If there are not a available connection, it will run auto_inuist.py. If you use it on Windows, you may need to use python /etc/auto_inuist.py instead of python3 /etc/auto_inuist.py (You must have installed Python3!).~~

`Net_test.sh` has been combined in `auto_nuist.py`.

---------

    */1 * * * * sh /etc/net_test.sh

`auto_nuist.py` will creat a file for crontab (It only works under Linux or Mac os.If you use Windows, you may need to use scheduled tasks). It is just a example. You should use `crontab -e` to creat a task to run `auto_nuist.py`.
You have to run `python3 auto_inuist.py` manually once before you can use crontab for automatic verification.

## Have fun！
