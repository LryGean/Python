# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

import jieba

f = "红楼梦.txt"
sf = "停用词.txt"
fi = open(f,"r",encoding="utf-8")
data = fi.read()
words = jieba.lcut(data)


sw = open(sf,'r',encoding='utf-8')
stopword = sw.read().split("\n")


namelist = [['凤姐','凤姐儿','凤丫头'],
            ['宝玉','二爷','宝二爷'],
            ['黛玉','颦儿','林妹妹','黛玉道'],
            ['宝钗','宝丫头'],
            ['贾母','老祖宗'],
            ['袭人','袭人道'],
            ['贾政','贾政道'],
            ['贾琏','琏二爷']]

for i in range(len(words)):
    if words[i] in stopword:
        words[i] = ''
    for j in range(8):
        if words[i] in namelist[j]:
            words[i] = namelist[j][0]

# 词频统计
d = {}
for i in words:
    d[i] = d.get(i,0) + 1
lt = list(d.items())
lt.sort(key=lambda x:x[1], reverse=True)        #递减排序


# 写入新文件
fo = open('result.csv','w')
for i in range(len(lt)):
    if lt[i][1] >= 40 and len(lt[i][0]) >= 2:
        fo.write('{},{}{}'.format(lt[i][0],lt[i][1],'\n'))

fi.close()
sw.close()
fo.close()
# items.sort(key=lambda x:x[1], reverse=True)
# 此行语句可以对items列表进行递减排序
  
