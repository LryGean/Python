# 第一步
from selenium import webdriver
import time

# 加载驱动
driver = webdriver.Chrome()

# 加载网站
driver.get('https://www.baidu.com/')
# 窗口最大化
driver.maximize_window()
# 隐式等待 没有找到元素，继续等待，超过时间抛出异常
driver.implicitly_wait(10)
# 强制性等待
time.sleep(2)


# 关闭当前的窗口
driver.close()
# 关闭所有窗口
# driver.quit()
