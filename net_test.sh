#!/bin/bash
PING=`ping -c 3 114.114.114.114 | grep '64 bytes' | wc -l`
NOT_PING="0"
if [ "$PING" -eq "$NOT_PING" ]
then
  python3 /etc/auto_inuist.py#python脚本目录
fi

