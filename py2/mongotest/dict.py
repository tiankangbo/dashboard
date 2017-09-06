# coding:utf8
__author__ = "tiankangbo"

dict1 = {
    'number':{
        'integer':{
            'ten':['1','2','3']
        }
    },
    'char':{
        'string':{
            'long':['abs', 'cbd', 'yur']
        }
    },
    'long':'00000000'
}

def list_all_dict(dict_a):
    if isinstance(dict_a, dict) : #使用isinstance检测数据类型
        for x in range(len(dict_a)):
            temp_key = dict_a.keys()[x]
            temp_value = dict_a[temp_key]
            print"%s : %s" %(temp_key,temp_value)
            list_all_dict(temp_value) #自我调用实现无限遍历

list_all_dict(dict1)