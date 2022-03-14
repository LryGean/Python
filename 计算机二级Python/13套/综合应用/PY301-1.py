#
# 请在此文件作答
#
import re

f_data = open('data.txt', 'r')
f_studs = open('studs.txt', 'w')
txt = f_data.readlines()
s = ""
for i in txt:
    l = re.split(':|,',i)
    s += "{}:{}".format(l[0],l[2])
f_studs.write(s[:-1])

f_data.close()
f_studs.close()
