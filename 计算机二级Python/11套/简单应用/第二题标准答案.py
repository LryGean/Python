import re


f = open('data.txt', 'r',encoding="utf-8")
dic = {}
for line in f:
    l = line.strip().split(',')
    if len(l)<3:
        continue
    else:
        dic[l[-1]] = dic.get(l[-1],[]) + [l[1]]
unis = list(dic.items())        
unis.sort(key=lambda x:len(x[1]),reverse=True)
for d in unis:
    print('{:>4}: {:>4} : {}'.format(d[0],len(d[1]),''.join(d[1])))