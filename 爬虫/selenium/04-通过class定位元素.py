from selenium import webdriver
from selenium.webdriver.common.by import By

# 加载驱动
driver = webdriver.Chrome()
# 加载网站
driver.get('https://www.baidu.com/')

# 旧方法
# driver.find_element_by_class_name('s_ipt').send_keys('皮卡丘')

# 新方法
driver.find_element(By.CLASS_NAME, 's_ipt').send_keys('猪八戒')
