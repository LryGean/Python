from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

# 加载驱动
driver = webdriver.Chrome()
# 加载网站
driver.get('https://www.17sucai.com/pins/demo-show?id=5926')
time.sleep(2)

# 若页面中有iframe标签，得先切入iframe标签
driver.switch_to.frame('iframe')
_tag = driver.find_element(By.ID, 'dk_container_country-nofake')
_tag.click()
time.sleep(2)
driver.find_element(By.XPATH, '//div[@class="dk_options"]/ul/li[2]a').click()

