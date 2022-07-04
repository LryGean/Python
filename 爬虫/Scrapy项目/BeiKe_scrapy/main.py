# 8.(必做题1)目标网站贝壳租房
# 网址：https://cs.zu.ke.com/zufang/rs/
# 需求：
# 1. 使用Scrapy爬取该网站前10页数据
# 2. 准备爬取的数据字段，分别是 房源标题（title）、所在区域（region）、所在街区（block）、
#                          小区（community）、房间面积（area）、朝向（toward）、
#                          户型（type）、租金（rent）、时间（time）。
# 3. 保存数据到bk.csv文件中

from scrapy import cmdline


cmdline.execute('scrapy crawl spider'.split())

