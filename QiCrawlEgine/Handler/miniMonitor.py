# coding:utf8
"""
-------------------------------------------------
   File Name：     miniMonitor.py
   Description :  测试程序,socket通讯
   Author :       tiankangbo
   date：         2017/10/12
-------------------------------------------------
   Change Activity:
                2017/10/16 修复import psutil的BUG
-------------------------------------------------
"""
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import time
import logging as p
import socketserver  # 导入socketserver模块
from Config.settings import host_settings


try:
    p.basicConfig(filename='../Log/miniMonitor.log',
                  format='%(asctime)s %(message)s',
                  filemode="w", level=p.DEBUG)
except Exception as e:
    raise e


try:
    import psutil
except:
    import os

    os.popen('apt-get install python-dev python-pip -y')
    os.popen('pip install psutil')
    import psutil


unit = {'b': 1, 'k': 2 ** 10, 'm': 2 ** 20, 'g': 2 ** 30}  # psutil 所采集的数据一般都是字节为单位.在这里定义换算字典
IP = host_settings['HOST']
PORT = host_settings['PORT']


class MyServer(socketserver.BaseRequestHandler):
    @staticmethod
    def getMessage(number):
        '''
        :param number: 进程号
        '''
        p = psutil.Process(pid=number)  # 实例化
        pname = p.name()
        ctime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(p.create_time()))  # 进程创建时间
        pcpu = p.cpu_percent()  # CPU使用率
        mem = p.memory_info().rss / unit['m']  # 占用内存MB
        pmen = p.memory_percent()  # 内存占用率
        wdata = p.io_counters().write_bytes / unit['k']  # 写入磁盘数据量KB
        return [number, pname, ctime, pcpu, pmen, mem, wdata]

    '''创建一个类，继承自socketserver模块下的BaseRequestHandler类'''

    def handle(self):
        '''
        :return:要想实现并发效果必须重写父类中的handler方法，在此方法中实现服务端的逻辑代码（不用再写连接准备，包括bind()、listen()、accept()方法）
        '''
        while True:
            try:
                conn = self.request
                addr = self.client_address
                # 上面两行代码，等于 conn,addr = socket.accept()，
                # 只不过在socketserver模块中已经替我们包装好了，还替我们包装了包括bind()、listen()、accept()方法
                while True:
                    accept_data = str(conn.recv(1024), encoding="utf8")
                    print("accept_data - ", accept_data, len(accept_data), type(accept_data))

                    try:
                        lt = self.getMessage(int(accept_data))
                        text = bytes(str(lt), encoding="utf8")
                        conn.sendall(text)

                    except:
                        if int(accept_data) in psutil.pids():
                            text = bytes('pid is exist, but not living, This could be a zombie process',
                                         encoding="utf8")
                        else:
                            text = bytes('pid is invalid', encoding="utf8")
                        conn.sendall(text)

                conn.close()

            except:
                mes = addr, '...break link'
                p.info(mes)
                break


def run_sk():
    try:
        sever = socketserver.ThreadingTCPServer((IP, PORT), MyServer)
        # 传入 端口地址 和 我们新建的继承自socketserver模块下的BaseRequestHandler类 实例化对象
        sever.serve_forever()  # 通过调用对象的serve_forever()方法来激活服务端
    except:
        raise Exception


if __name__ == '__main__':
    run_sk()
