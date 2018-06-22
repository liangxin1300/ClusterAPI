#!/bin/bash

ps -ef|grep "ClusterAPI/api.py"|grep -v grep &> /dev/null
if [ "$?" -ne 0 ];then
    python3 /opt/ClusterAPI/api.py &> /dev/null &
fi
