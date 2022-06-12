from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# 加载驱动
driver = webdriver.Chrome()
# 加载网站
driver.get('https://qzone.qq.com/')
# 获取百度cookie
cookies = driver.get_cookies()
driver.switch_to.frame('login_frame')
driver.find_element(By.ID, 'img_out_897704091').click()
cookies = driver.get_cookies()
time.sleep(2)
li = []
for cookie in cookies:
    name = cookie['name']
    value = cookie['value']
    li.append(f'{name}={value}')
#
cookie = '; '.join(li)
print(cookie)
