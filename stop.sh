#!/bin/bash

pid=`ps -ef|grep "ClusterAPI/api.py"|grep -v grep|awk '{print $2}'`
if [ -n "$pid" ];then
    kill -9 $pid
fi
