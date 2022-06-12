from selenium import webdriver
from selenium.webdriver.common.by import By

# 加载驱动
driver = webdriver.Chrome()
# 加载网站
driver.get('https://www.baidu.com/')

driver.find_element_by_css_selector('#kw').send_keys('孙悟空')


