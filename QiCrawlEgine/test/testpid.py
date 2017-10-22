import psutil

pid = 18012
num = 0
a = psutil.Process(pid=pid)

while num < 1000:
    num = num + 1
    print(a.status())