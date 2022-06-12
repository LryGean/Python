# 第一步
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 加载驱动
driver = webdriver.Chrome()

# 加载网站
driver.get('https://www.baidu.com/')

# 显示等待，默认0.5
element = WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.ID, 'kw')))
element.send_keys('hello')
