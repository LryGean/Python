from selenium import webdriver
from selenium.webdriver.common.by import By

# 加载驱动
driver = webdriver.Chrome()
# 加载网站
driver.get('https://www.baidu.com/')

# 查找一个元素
# input_tag = driver.find_element_by_tag_name('input')
# print(type(input_tag))

# 多个
input_tags = driver.find_elements_by_tag_name('input')
print(input_tags)
