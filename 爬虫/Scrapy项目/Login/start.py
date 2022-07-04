import time

from scrapy import cmdline

t1 = time.time()
cmdline.execute('scrapy crawl spider1'.split())
t2 = time.time()
print(t2-t1)




