# coding:utf8
import re

#pattern = re.compile(r'text|image|audio')
# pattern = re.compile(r'\btex?t?\b|\bimag?e?\b|\bau?v?dio\b')
#
#
# s = '*.xml text/xml, te, tex,text, application/xml audio/mp4, image/png'
#
# result = re.findall(pattern, s)
# print result
"""
正则表达式的几种模糊匹配方式
"""

# color还是colour
pattern_1 = re.compile(r'\bcolou?r\b')

# cat还是hat
pattern_2 = re.compile(r'\b[ch]at\b]')

# doc结尾的单词
pattern_3 = re.compile(r'\b\w*doc\b')

# Steve、 Steven还是Step
pattern_4 = re.compile(r'\bSte(?:ven?|p)\b')

# 单词变体猜测 regular 或expression
pattern_5 = re.compile(r'\breg(?:ular·expressions?|ex(?:ps?|e[sn])?)\b')


s = "color colour cat net Steven, a.doc, regular"
result = re.findall(pattern_1, s)

print result