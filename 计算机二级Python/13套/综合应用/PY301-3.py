#
# 请在此文件作答
#
import re

f_data = open('data.txt', 'r')
f = f_data.readlines()
d = {}
d1 = {}
sum = 0
l = []
for i in f:
    s = []
    a = re.split(':|,',i)
    s.append(a[1])
    s.append(a[2][:-1])
    l.append(s)
for i in l:
    d[i[0]] = d.get(i[0],0) + 1
    d1[i[0]] = d1.get(i[0],0) + int(i[1])
print(d)
print(d1)
for i in d.keys():
    ch = '{0}:{1:.2f}'.format(i,d1[i]/d[i])
    print(ch)
f_data.close()