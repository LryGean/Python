# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# # 加载驱动
# driver = webdriver.Chrome()
# # 加载网站
# driver.get('https://www.17sucai.com/pins/demo-show?id=5926')
# time.sleep(2)
#
# # 若页面中有iframe标签，得先切入iframe标签
# driver.switch_to.frame('iframe')
# driver.find_element(By.CLASS_NAME, 'nojs').click()

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
# 实例化Select
select_tag = Select(driver.find_element(By.CLASS_NAME, 'nojs'))
# 根据属性值定位
# select_tag.select_by_value('CA')
# 根据索引，索引是从0开始的
select_tag.select_by_index(1)
