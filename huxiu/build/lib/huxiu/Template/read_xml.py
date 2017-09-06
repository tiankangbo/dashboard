# coding:utf8
__author__ = 'tiankangbo'
'''函数功能：读取xml内的标签值'''

import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from xml.dom.minidom import parse

def getText(nodelist):
    # 判断数值是否是TEXT_NODE，从而进行取值
    nd = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            nd = nd + node.data
    return nd

def getxml(de_val):
    # 从xml路径获取xml的标签值
    global val
    dom1 = parse('huxiu.xml')  # 路径可以更改
    config_element = dom1.getElementsByTagName("config")[0]
    servers = config_element.getElementsByTagName(de_val)
    for server in servers:
        val = getText(server.childNodes)
    return val

def get_val():
    #由自定义标签检索xml文件，从而获取配置文件的参数
    lists = []
    #手动列出需要检索的xml标签
    de_val = ["name", "domain", "title", "author", "text", "posttime", "link", "instime"]
    for i in de_val:
        lists.append(getxml(i))
    return lists

if __name__ == "__main__":

    print(get_val())
