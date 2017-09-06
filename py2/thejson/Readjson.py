import json


def loadFont():

    f = open("firstjson", encoding='utf8')

    setting = json.loads(f)

    family = setting['BaseSettings']['size']

    return family

t = loadFont()

print t
