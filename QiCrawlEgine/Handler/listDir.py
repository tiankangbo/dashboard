# coding:utf8
"""
-------------------------------------------------
   File Name：     lisrDir.py
   Description :  自动检索新加入的爬虫单线程文件
   Author :       tiankangbo
   date：         2017/10/09
-------------------------------------------------
   Change Activity:
-------------------------------------------------
"""
import os
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


def listDir(strd):
    '''
    :param strd: 爬虫单线程文件的包路径
    :return: 返回该包下面所有的爬虫单线程文件名
    '''
    return [names.split('.')[0] for names in os.listdir(path=strd) if
            (names.endswith('.py') and '__init__.py' != names)]


if __name__ == '__main__':
    strd = "../Spiders"
    print(listDir(strd)[0], listDir(strd)[1], listDir(strd)[2])
