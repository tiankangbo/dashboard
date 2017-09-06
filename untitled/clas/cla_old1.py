class Foo(object):

    def __init__(self):
        self.name = 'tiankangbo'

    def func(self):
        return 'func'

obj = Foo()

hasattr(obj, 'name')
hasattr(obj, 'func')


print getattr(obj, 'name')
print getattr(obj, 'func')

print setattr(obj, 'age', 18)
print setattr(obj, 'show', lambda num: num+1 )

