#
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 加载驱动
driver = webdriver.Chrome()
# 加载网站
driver.get('https://movie.douban.com/top250')
time.sleep(2)
driver.find_element(By.LINK_TEXT, '后页>').click()
time.sleep(1)
print(driver.page_source)
