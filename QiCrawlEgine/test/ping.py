# from subprocess import Popen
#
# try:
#     text = 'ping -c 4 -w 5 www.baidu.com'
#     process = Popen(text, shell=True)
#     process.communicate()
#
# except Exception as e:
#     raise e



# def ping():
#     '''测试网络环境'''
#     import os
#     import subprocess
#
#     try:
#         fp = open(os.devnull, 'w')
#         reta = subprocess.call('ping -c 6 -w 5 www.baidu.com', stdout=fp, stderr=fp, shell=True)
#         print("reta", reta)
#         if reta:
#             fp.close()
#             return '0'
#
#         else:
#             fp.close()
#             return '1'
#
#     except Exception as e:
#         print(e)
#
# print(ping())



def ping():
    '''测试网络环境'''
    import os
    import subprocess

    try:
        return subprocess.call('ping -c 5 -w 5 www.baidu.com', stdout=open('/dev/null', 'w'), stderr=subprocess.STDOUT, shell=True)

    except Exception as e:
        print(e)

print(ping(), type(ping()))