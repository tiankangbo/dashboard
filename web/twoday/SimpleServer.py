class WSGIapp(object):
    def __init__(self):
        self.routes = {}

    def route(self, path=None):
        def decorator(func):
            self.routes[path] = func
            print "func->", func
            print "self.route[path]", self.routes[path]
            return func
        return decorator

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        if path in self.routes:
            status = '200 OK'
            response_headers = [('Content-Type', 'text/plain')]
            start_response(status, response_headers)
            return self.routes[path]()
        else:
            status = '404 Not Found'
            response_headers = [('Content-Type', 'text/plain')]
            start_response(status, response_headers)
            return '404 Not Found!'

app = WSGIapp()

@app.route('/')
def index():
    return ['index']

@app.route('/hello')
def hello():
    return ['hello world']

from wsgiref.simple_server import make_server
httpd = make_server('', 8888, app)
httpd.serve_forever()