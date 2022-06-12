# text:获取节点子节点和后代文本内容

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 加载驱动
driver = webdriver.Chrome()
# 加载网站
driver.get('https://movie.douban.com/top250')
div_tag = driver.find_element(By.XPATH, '//div[@class="hd"]')
print(div_tag.text)


