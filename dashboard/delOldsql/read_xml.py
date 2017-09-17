# coding:utf8
"""
-------------------------------------------------
   File Name：     read_xml.py
   Description :
   Author :       tiankangbo
   date：         2017/3/13
-------------------------------------------------
   Change Activity:
-------------------------------------------------
"""
'''函数功能：读取xml内的标签值'''

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
    dom1 = parse('/dashboard/delOldsql/config')  # 路径可以更改
    #dom1 = parse('../net/config')  # parse an XML file by name
    config_element = dom1.getElementsByTagName("config")[0]
    servers = config_element.getElementsByTagName(de_val)
    #print "servers : ", type(servers), servers
    for server in servers:
        val = getText(server.childNodes)
    return val

def get_val():
    #由自定义标签检索xml文件，从而获取配置文件的参数
    lists = []
    #手动列出需要检索的xml标签
    de_val = ["server", "port", "user", "pwd", "db", "time",]
    for i in de_val:
        lists.append(getxml(i))
    return lists

if __name__ == "__main__":

    print get_val()
