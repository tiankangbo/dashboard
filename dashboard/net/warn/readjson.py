# coding:utf8
"""
-------------------------------------------------
   File Name：     read_json.py
   Description :  读取json数据
   Author :       tiankangbo
   date：         2017/3/13
-------------------------------------------------
   Change Activity:
-------------------------------------------------
"""

import json
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def load():
    with open('/dashboard/net/warn/warning.json', 'r') as json_file:
        command_in = json.load(json_file)
    json_file.close()
    return command_in


def usage_command(comm):
    data = load()
    return data[comm]


if __name__ == "__main__":

    print usage_command("cpu_stat1")