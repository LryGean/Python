
import re
from urllib import request

from numpy import number

# 断点调试

class Spider():
    # 网页地址
    url = 'https://www.huya.com/g/lol'    # LOL
    # url = 'https://www.huya.com/g/489'  # 梦三国


    # 正则表达式
    # 匹配<span class="txt"></span>内的所有字符
    # *号代表0次或多次
    # ?号代表非贪婪模式，可以在最近的<\span>进行结束匹配
    root_pattern = '<span class="txt">([\s\S]*?)</li>'   # 定位标签
    name_pattern = '<i class="nick" title="([\s\S]*?)">'
    number_pattern = '<i class="js-num">([\s\S]*?)</i>'


    # 私有方法
    def __fetch_content(self):
        # 抓取网页地址
        r = request.urlopen(Spider.url)

        # 数字bytes表示字节码
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')

        return htmls


    # 分析    
    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        anchors = []
        
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            # print("姓名：",name,"\n" + "人气量：",number)
            # print("-------------------------------------------")
            # 将获取到的名字和人气量拼成字典形式
            anchor = {'name':name, 'number':number}
            anchors.append(anchor)
        # print(anchors)
        # print(anchors[0]['name'][0])
        
        return anchors


    # 精炼(规范数据)
    # 方法一：lambda表达式
    def __refine0(self, anchors):
        l = lambda anchor:{
            'name':anchor['name'][0],
            'number':anchor['number'][0]
            }
        return map(l, anchors)

    # 方法二：for循环
    # def __refing1(self,anchors):
    #     anc = []
    #     for anchor in anchors:
    #         an = {
    #             'name':anchor['name'][0],
    #             'number':anchor['number'][0]
    #             }
    #         anc.append(an)
    #     return anc


    # 排序
    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort__seed, reverse=True)
        return anchors
    
    def __sort__seed(self, anchor):
        r = re.findall('\d*',anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number



    def __show(self, anchors):
        # for anchor in anchors:
        #     print(anchor['name'] + '---------' + anchor['number'])
        for rank in range(0, len(anchors)):
            print('rank ' + str(rank+1)
                  + '  :  ' +  anchors[rank]['name']
                  + '     ' + anchors[rank]['number']    
            )


    # __fetch_content的入口方法
    def go(self): 
        htmls = self.__fetch_content()           # 获取数据
        
        anchors = self.__analysis(htmls)         # 分析数据 

        anchors = list(self.__refine0(anchors))  # 精炼数据
        # anchors = self.__refing1(anchors)
        
        anchors = self.__sort(anchors)           # 排序数据

        self.__show(anchors)                     # 展示数据

        # print(anchors)

spider = Spider()
spider.go()



# Ctrl+o:快捷定位函数位置