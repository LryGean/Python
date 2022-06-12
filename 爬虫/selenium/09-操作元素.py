from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 加载驱动
driver = webdriver.Chrome()
# 加载网站
driver.get('https://www.baidu.com/')

input_tag = driver.find_element_by_id('kw')
input_tag.send_keys('python')

time.sleep(3)
# 清除内容
input_tag.clear()

# 定位元素
# driver.find_element_by_id('su').click()

