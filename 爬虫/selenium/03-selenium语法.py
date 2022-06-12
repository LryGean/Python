# 需求：定位输入框
from selenium import webdriver
from selenium.webdriver.common.by import By


# 加载驱动
driver = webdriver.Chrome()
# 加载网站
driver.get('https://www.baidu.com/')
# 定位输入框，写入内容
# 新方法
driver.find_element(By.ID, 'kw').send_keys('皮卡丘')
