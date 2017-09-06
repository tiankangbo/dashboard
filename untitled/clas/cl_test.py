class Foo(object):

    def __init__(self):
        self.name = 'tian'

    def func(self):
        return 'func'

obj = Foo()

print obj.name

print obj.func()

print obj.__dict__['name']