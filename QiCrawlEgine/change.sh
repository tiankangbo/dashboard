#!/bin/bash
# coding:utf8

aa="sources.list"

#主流程
if [ -n $aa ];then
  touch $aa
  echo "1->ali(ubuntu16) 2->ali(ubuntu14) 3->nyist(ubuntu14)"
  echo "choose :"
  read sou_name #由键盘读入源类型，切换源

  if [ "$sou_name" = 1 ];then
    echo "${aa}文件已经创建完毕。。。开始写入${sou_name}源地址"
    echo "deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse " >> $aa
    echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse" >> $aa
    echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse" >> $aa
    echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse" >> $aa
    echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted universe multiverse" >> $aa

  elif [ "$sou_name" = 2 ];then
    echo "${aa}文件已经创建完毕。。。开始写入${sou_name}源地址"
    echo "deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse" > $aa
    echo "deb http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse" >> $aa
    echo "deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse" >> $aa
    echo "deb http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse" >> $aa
    echo "deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse" >> $aa

  elif [ "$sou_name" = 3 ];then
    echo "${aa}文件已经创建完毕。。。开始写入${sou_name}源地址"
    echo "deb http://59.69.128.21/ubuntu/ trusty main restricted universe multiverse" > $aa
    echo "deb http://59.69.128.21/ubuntu/ trusty-security main restricted universe multiverse" >> $aa
    echo "deb http://59.69.128.21/ubuntu/ trusty-updates main restricted universe multiverse" >> $aa
    echo "deb http://59.69.128.21/ubuntu/ trusty-proposed main restricted universe multiverse" >> $aa
    echo "deb http://59.69.128.21/ubuntu/ trusty-backports main restricted universe multiverse" >> $aa
  else
    exit 1
  fi
  rm -rf /etc/apt/sources.list
  mv $aa /etc/apt/
else
  echo "error"
fi

#测试写入源是否成功
if test -s /etc/apt/sources.list;then
  cat /etc/apt/sources.list
  apt-get update

  echo "Do you need to upgrade the software? y/n"
  read option
  if [ "$option" = 'y' ];then
    apt-get -y upgrade
  else
    echo "not upgrade"
  fi
else
  echo "empty"
fi

