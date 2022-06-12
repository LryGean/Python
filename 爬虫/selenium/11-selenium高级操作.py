# 网页源码  —— page source

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 加载驱动
driver = webdriver.Chrome()
# 加载网站
driver.get('https://music.163.com/#/discover/toplist')
time.sleep(2)
# 若页面中有iframe标签，得先切入iframe标签
driver.switch_to.frame('g_iframe')
time.sleep(2)
html = driver.page_source  # 拿到网页源码
print(html)

