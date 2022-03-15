import json   # 数据类型转换
import requests  #对网站发送请求
import jsonpath  #提取数据
from pyecharts.charts import Map  #绘制地图  pycharts:动态
from pyecharts import options as opts
from demo1 import nameMap

#1.试试抓取数据   提取国家名字+数量
url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist'   #网站接口数据
resp = requests.post(url).text   #post请求方式 get text:获取源代码
# print(resp)  # 源代码
# print(type(resp))

#string字符串--dict字典
data = json.loads(resp)
# print(data)

# 从网页源代码 提取数据，name名字+confirm病死率  bs4 lxml pyquery re ...
name = jsonpath.jsonpath(data,'$..name')  # $: 代表最外层的字典{}   ..name匹配的数据
# print(name)

confirm = jsonpath.jsonpath(data,'$..confirm')
# print(confirm)

a = list(zip(name,confirm))  # zip：把两组数据进行
# print(a)

#2.数据可视化展示  地图绘制
map_ = Map(opts.InitOpts(width='1200px',height='600px')).add(series_name='世界各国病死率',
                                                             data_pair=a,
                                                             maptype='world', 
                                                             name_map=nameMap,
                                                             is_map_symbol_show=False,              
                                                            )

#不显示国家名称
map_.set_series_opts(label_opts=opts.LabelOpts(is_show=False))

#颜色 左上角名称  图例
map_.set_global_opts(title_opts=opts.TitleOpts(title='国外疫情情况'),
                    visualmap_opts=opts.VisualMapOpts(max_=40000000,is_piecewise=True))

map_.render('国外疫情情况.html')

