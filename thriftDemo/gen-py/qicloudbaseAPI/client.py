# coding:utf8
__author__ = 'tiankangbo'

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import time
from QicloudBaseApiServer import *
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


class WorkClient(object):
    def __init__(self, host, port):
        # init是初始化了与thrift服务连接的情况
        self.host = host
        self.port = port
        self.transport = TSocket.TSocket(host, port)
        self.transport = TTransport.TBufferedTransport(self.transport)
        self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)

    def mk_conn(self):
        # 创建socket链接，并打开链接
        self.client = Client(self.protocol)
        self.transport.open()

    def close_conn(self):
        # 关闭socket链接
        self.transport.close()

    def work_for_ping(self):
        # 测试ping通服务器端
        return self.client.Ping("123")


    '''版本'''
    def get_version(self):
        return self.client.send_GetVersionInfo()


    '''模板测试模块'''
    def work_for_listTemplate(self):
        # 模板列表
        return self.client.getTempalteInfoList()

    def work_for_oneTemplate(self, id):
        # 获取某个特定的节点信息
        return self.client.getTemplateInfo(id)

    def work_for_addTemplate(self, user, name, type, OStype ,OSversion):
        # 添加一个模板
        info = QiTemplateInfo()
        info.username = user
        info.name = name
        info.type = type
        info.OStype = OStype
        info.OSversion = OSversion
        self.client.addTemplateInfo(info)

    def work_for_delTemplate(self, id):
        # 删除某个模板
        self.client.delTemplateInfo(id)

    def work_for_setTemplate(self):
        # 修改特定模板信息
        pass


    '''存储测试模块'''
    def work_for_storageList(self):
        # 存储列表
        return self.client.getStorageInfoList()

    def work_for_addStorage(self, ip, name):
        # 添加存储
        info = QiStorageInfo()
        info.ip = ip
        info.name = name
        self.client.addStorageInfo(info)

    def work_for_delStorage(self, ip):
        # 删除存储
        self.client.delStorageInfo(ip)


    '''节点测试模块'''
    def work_for_listHost(self):
        # 节点列表
        return self.client.getHostInfoList()

    def work_for_addHost(self, ip, name):
        # 添加一个节点
        info = QiHostInfo()
        info.name = ip
        info.ip = name
        self.client.addHostInfo(info)
        #print ">>> %s 已经成为一个节点" % info

    def work_for_delHost(self, ip):
        # 删除一个结点
        self.client.delHostInfo(ip)
        #print ">>> %s 已经从节点中移除" % ip

    def get_for_oneHost(self, ip):
        # 获取某个特定节点的信息
        self.client.getHostInfo(ip)

    def set_for_oneHost(self, ip, name):
        # 更改某节点信息
        pass


    '''虚拟机instance测试模块'''
    def work_for_listInstance(self):
        # 虚拟机列表
        return self.client.getAllInstanceInfoList()

    def work_for_instanceInfo(self, uuid):
        # 获取某个实例信息
        return self.client.getInstanceInfo(uuid)

    def work_createInstance(self):
        pass

    def work_startInstance(self, uuid, disprotocol):
        # 启动实例
        info=QiHostInfo()
        self.client.startInstance(info, uuid, disprotocol)

    def work_delInstance(self):
        pass

    def for_addInterface(self):
        pass

    def for_delInterface(self):
        pass

    def for_addDisk(self):
        pass

    def for_delDisk(self):
        pass

    def for_addISO(self):
        pass

    def for_delISO(self, uuid):
        # 移除ISO文件
        self.client.instanceRemoveISOFile(uuid)

    def shutdown_instance(self, uuid):
        # 给某个实例关机
        self.client.shutdownInstance(uuid)

    def poweroff_instance(self):
        pass

    def reset_instance(self):
        pass


if __name__ == '__main__':
    '''实例化一个对象'''
    a = WorkClient('192.168.25.171', 9090)
    #连接
    a.mk_conn()

    '''功能测试'''
    print a.work_for_ping()
    # print a.get_version()

    # 节点
    # print "节点列表 -- ", a.work_for_listHost()
    #print "删除节点测试--192.168.25.191", a.work_for_delHost('192.168.25.191')
    #print "添加节点测试 -- ", a.work_for_addHost('192.168.25.191', '191')
    #print "获取某个指定节点的信息 -- ", a.get_for_oneHost('192.168.25.145')

    # 存储
    #print "存储列表 -- ", a.work_for_storageList()
    #print "添加存储 -- ", a.work_for_addStorage('')
    #print "删除存储 -- ", a.work_for_delStorage('')

    # 模板
    # print "模板列表 -- ", a.work_for_listTemplate()
    #print "获取某个指定模板的信息 -- ", a.work_for_oneTemplate('disk.qcow2')
    # print "删除某一个模板 -- ", a.work_for_delTemplate('disk.qcow2')
    # print "添加一个模板 -- ", a.work_for_addTemplate('xiaoming', 'test', '1', 'windows', 'win7')

    # 虚拟机
    print "实例列表", a.work_for_listInstance()
    # print "获取某个实例信息 -- ", a.work_for_instanceInfo('09c435ac-cc37-4cf1-8044-5f7d92c294ac')
    # print "简单的启动某个实例 -- ", a.work_startInstance('09c435ac-cc37-4cf1-8044-5f7d92c294ac', 1)
    # time.sleep(3)
    # print "关机 -- ", a.shutdown_instance('09c435ac-cc37-4cf1-8044-5f7d92c294ac')
    # time.sleep(3)
    # print "获取某个实例信息 -- ", a.work_for_instanceInfo('09c435ac-cc37-4cf1-8044-5f7d92c294ac')
    print "移除ISO", a.for_delISO('09c435ac-cc37-4cf1-8044-5f7d92c294ac')
    print "获取某个实例信息 -- ", a.work_for_instanceInfo('09c435ac-cc37-4cf1-8044-5f7d92c294ac')
    # print "实例列表", a.work_for_listInstance()

    '''关闭链接'''
    a.close_conn()
