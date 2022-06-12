from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 加载驱动
driver = webdriver.Chrome()
# 加载网站
driver.get('https://movie.douban.com/subject/1292052/')
img_tag = driver.find_element(By.XPATH, '//div[@id="mainpic"]/a/img')
print(img_tag.get_attribute('src'))  # 获取属性值
