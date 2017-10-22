# coding:utf8
"""
-------------------------------------------------
   File Name：     runQicrawlEgine.py
   Description :  启动tornado文件
   Author :       tiankangbo
   date：         2017/9/25
-------------------------------------------------
   Change Activity:
-------------------------------------------------
"""
import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import time
import logging
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen

from concurrent.futures import ThreadPoolExecutor
from tornado.concurrent import run_on_executor
from Handler.control import schedulerQi, stopProcess
from Handler.dbClient import MysqlDB
from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)
'''平台性能调节(0代表开启最大进程数, 与服务器核数有关, 1,2,3..开启的进程数目)'''
num_processes = 2
path = "/root/PycharmProjects/QiCrawlEgine/Spiders/Image/"


try:
    logging.basicConfig(filename='../Log/logging.log',
                        format='%(asctime)s %(message)s',
                        filemode="w", level=logging.DEBUG)
except Exception as e:
    raise e


class MyHandler(tornado.web.RequestHandler):
    '''
    class: MyHandler
    类功能: 用来处理post请求, 当第三方发出post请求的时候, MyHandler类会异步处理post的请求参数,
        分析请求参数以后, 开启任务调度器.
    '''
    executor = ThreadPoolExecutor(max_workers=128)

    def filterJob_(self, username, template):
        '''
        :param pid: post请求中, 根据模板名字做出判断,该用户所操作的job里是否含有相同任务是处于开启中的State==1
        :return:函数功能 ->如果该用户所操作的任务中, 已经有相同job的State==1,则不能继续开启任务
        '''
        try:
            sql_ft = 'select State from spiderinfo where Username="{}" AND template="{}"'.format(str(username),
                                                                                              str(template))
            return ['1' for key, item in enumerate(MysqlDB().select_(sql=sql_ft)[0]) if '1' in item[0]][0]

        except Exception as e:
            logging.info(e)

    @tornado.gen.coroutine
    def startJob_(self, user_, jobname_, key_, template_, date_in_, id_):
        '''
        :param user_: 用户名
        :param jobname_: 任务名字
        :param key_: 关键字
        :param template_: 任务模板
        :param date_in_: 采集数据日期搜索范围
        :param id_: 用户id
        :return: 函数共功能 -> 开启一条爬虫任务
        '''
        job_ = schedulerQi(username=user_, jobname=jobname_, keyword=key_, template=template_, date_in=date_in_)
        job_.start()

        logging.info((jobname_, user_, template_, '...starting'))

        try:
            sql_st = 'update spiderinfo set Jobid={}, State={}, Starttime={}, Endtime={} where id={}'.format(
                str(job_.pid), '1', str(time.time()), '0', int(id_))
            MysqlDB().update_(sql=sql_st)

            sql_test = 'select * from spiderinfo where id={}'.format(str(id_))  # 测试
            print('开启状态 -- ', MysqlDB().select_(sql_test))  # 打印

            job_.join()

            logging.info((jobname_, user_, template_, '...stoping'))

        except Exception as e:
            logging.info(e)

        try:
            '''任务执行完毕,修改State为0'''
            sql_up = 'update spiderinfo set State={}, Endtime={} where id={}'.format('0', str(time.time()), int(id_))
            MysqlDB().update_(sql=sql_up)

            print('结束状态 -- ', MysqlDB().select_(sql_test))  # 打印

        except Exception as e:
            logging.info(e)

    @tornado.gen.coroutine
    def stopJob_(self, id_, template_, jobid_):
        '''
        :param id_: 用户id
        :param template_: 任务模板
        :param jobid_: 任务id
        :return: 函数功能 -> 中断爬虫任务
        '''
        proc = stopProcess(str(jobid_))
        proc.stop_()

        logging.info((jobid_, template_, '...Interrupt'))

        '''中断,修改任务State为0'''

        try:
            sql_tp = 'update spiderinfo set State={}, Endtime={} where id={}'.format('0', str(time.time()), int(id_))
            MysqlDB().update_(sql=sql_tp)

        except Exception as e:
            logging.info(e)

    @run_on_executor
    def takeJob_(self, dic):
        '''
        :param dic: post请求参数
        :return: 函数功能 -> 分析post请求, 生成任务
        '''
        try:
            id_ = dic['id']
            user_ = dic['Username']
            template_ = dic['Template']
            jobname_ = dic['Jobname']
            jobid_ = dic['Jobid']
            state_ = dic['State']
            key_ = dic['Keyword']
            date_in_ = dic['Searchdate']

            if '1' == state_:
                '''用户post请求开启任务'''
                if '1' == self.filterJob_(user_, template_):
                    logging.info((jobname_, user_, template_, '开启任务异常, 或有相同任务未结束'))

                else:
                    self.startJob_(user_, jobname_, key_, template_, date_in_, id_)

            elif '0' == state_:
                self.stopJob_(id_, template_, jobid_)

            else:
                logging.info('状态码无效')

        except Exception as e:
            logging.info(e)

    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        '''
        :return: 函数功能 -> 接收post请求, 处理完毕post请求以后, 调用add_callback()做延时操作的函数分离
        '''
        try:
            data = self.request.body
            self.write(data)
            tornado.ioloop.IOLoop.instance().add_callback(callback=lambda: self.takeJob_(eval(data)))

        except Exception as e:
            logging.info((e, '请求开启爬虫失败'))


class getOne(tornado.web.StaticFileHandler):
    @tornado.gen.coroutine
    def set_extra_headers(self, path):
        self.set_header("Cache-control", "no-cache")


'''路由信息'''
app = tornado.web.Application(
    handlers=[
        (r"/request", MyHandler),
        (r"/get/(.*)", getOne, {"path": path}),
    ],
    debug=False,
)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(options.port)
    http_server.start(num_processes)
    tornado.ioloop.IOLoop.instance().start()