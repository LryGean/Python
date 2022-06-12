# 需求：定位输入框
from selenium import webdriver
import time

# 加载驱动
driver = webdriver.Chrome()
# 加载网站
driver.get('https://www.baidu.com/')
# 定位输入框，写入内容

driver.find_element_by_id('kw').send_keys('python')   # 旧方法


