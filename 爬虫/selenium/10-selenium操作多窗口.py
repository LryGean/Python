from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 加载驱动
driver = webdriver.Chrome()
# 加载网站
driver.get('https://www.baidu.com/')

# 打开第二个窗口
driver.execute_script('window.open("https://www.douban.com/")')

time.sleep(3)

#
# driver.find_element(By.id, 'kw').send_keys("python")

# 切换页面
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
print(driver.current_url)  # 当前页面的url
driver.switch_to.window(driver.window_handles[1])  # 或-1
print(driver.current_url)  # 当前页面的url
