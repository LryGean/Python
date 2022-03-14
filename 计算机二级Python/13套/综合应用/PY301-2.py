#
# 请在此文件作答
#
import re
f_data = open('data.txt', 'r')
txt = f_data.readlines()
l = []
for i in txt:
    s = []
    a = re.split(':|,',i)
    s.append(a[0])
    s.append(a[2][:-1])
    l.append(s)
print(l)
l.sort(key=lambda x:x[1], reverse=True)
print("{}:{}".format(l[0][0],l[0][1]))
f_data.close()