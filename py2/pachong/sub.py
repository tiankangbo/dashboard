# coding:utf8

import re

p = re.compile(r'(?P<word1>\w+) (?P<word2>\w+)') # 使用名称引用

s = 'i say, hello world ,a b!'
print p.sub(r'\g<word2> \g<word1>', s)

p = re.compile(r'(\w+) (\w+)') #使用编号
print p.sub(r'\2 \1', s)

def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()

print p.sub(func, s)