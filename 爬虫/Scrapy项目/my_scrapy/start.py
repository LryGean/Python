import time

from scrapy import cmdline

t1 = time.time()
# cmdline.execute('scrapy crawl spider -o demo.csv'.split())
cmdline.execute('scrapy crawl spider2'.split())
t2 = time.time()
print(t2-t1)




