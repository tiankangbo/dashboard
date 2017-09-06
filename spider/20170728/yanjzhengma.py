# coding:utf8
__author__ = 'tiankangbo'

import pytesseract
from PIL import Image

try:

    image = Image.open('7039.jpg')

    code = pytesseract.image_to_string(image)
    print "code的值", code

except Exception, e:
    print e

# print "code的值", code
