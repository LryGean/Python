from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time

# 加载驱动
driver = webdriver.Chrome()
# 加载网站
driver.get('https://kuwo.cn/')
driver.find_element(By.CLASS_NAME, 'search').send_keys('一起逃命')
driver.find_element(By.CLASS_NAME, 'search').send_keys(Keys.ENTER)  # 回车键
time.sleep(2)
# 实例化对象
actions = ActionChains(driver)
# 歌曲位置
element = driver.find_element(By.XPATH, '//ul[@class="search_list"]/li[1]')
# 移动操作
actions.move_to_element(element)
# 提交
actions.perform()
# 点击播放按钮， 点击实销
# driver.find_element(By.XPATH, '//div[@class="song_opts flex_c"]/i[1]').click()

# 执行js代码进行点击
ele = driver.find_element(By.XPATH, '//div[@class="song_opts flex_c"]/i[1]')
driver.execute_script("arguments[0].click()", ele)

