# coding:utf-8

import json


def load():
    with open('/home/tiankango/PycharmProjects/cloudstack0/cloudA/corefile/commands.json', 'r') as json_file:
        command_in = json.load(json_file)
    json_file.close()
    return command_in


def usage_command(comm):
    data = load()
    return data[comm]


if __name__ == "__main__":

    print usage_command(["baseurl"])