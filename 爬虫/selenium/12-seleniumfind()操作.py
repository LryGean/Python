# find：在HTML结构源码中查找某个字符是否存在
"""
1-100
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# 加载驱动
driver = webdriver.Chrome()
# 加载网站
driver.get('https://www.baidu.com/')
time.sleep(1)

# 存在的字符返回的是数值，不存在的返回-1
print(driver.page_source.find('kw'))
print(driver.page_source.find('wd'))
