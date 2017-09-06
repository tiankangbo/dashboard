# from gevent import monkey
#
# monkey.patch_all()
# from flask import Flask
# from gevent import pywsgi
# import time
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def index():
#     for i in range(10):
#         print(i)
#         time.sleep(2)
#     return "hello"
#
#
# server = pywsgi.WSGIServer(('127.0.0.1', 5000), app)
# server.serve_forever()
from flask import Flask
import time
from multiprocessing import Process

app = Flask(__name__)

class MyProcess(Process):
    def __init__(self):
        Process.__init__(self)

    def run(self):
        for i in range(10):
            print(i)
            time.sleep(2)

@app.route('/')
def hello_world():
    job = MyProcess()
    job.daemon = True
    job.start()
    # job.join()
    return 'Hello World!'

if __name__ == '__main__':
    app.run()