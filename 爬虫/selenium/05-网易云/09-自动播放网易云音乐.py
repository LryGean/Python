from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 加载驱动
driver = webdriver.Chrome()
# 加载网站
driver.get('https://music.163.com/')

input_tag = driver.find_element_by_id('srch')
input_tag.send_keys('Tomorrow will be fine')

time.sleep(1)
input_tag.send_keys(Keys.ENTER)
time.sleep(2)
# 若页面中有iframe标签，得先切入iframe标签
driver.switch_to.frame('g_iframe')
driver.find_element_by_id('song_1425676569').click()

