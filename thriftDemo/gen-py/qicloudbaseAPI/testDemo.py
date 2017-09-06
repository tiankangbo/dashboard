# coding:utf8
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from QicloudBaseApiServer import *
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
    # 创建socket
    transport = TSocket.TSocket('192.168.25.171', 9090)

    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    client = Client(protocol)
    transport.open()


    print client.Ping("123")
    print u"存储列表", client.getStorageInfoList()
    print u"模板",client.getTempalteInfoList()
    #print u"get version-->",client.getTemplateInfo(1)
    print u"虚拟机列表", client.getAllInstanceInfoList()

    transport.close()

except Thrift.TException, ex:
    print "%s" % (ex.message)
