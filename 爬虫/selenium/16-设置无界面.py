from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. 创建对象
options = webdriver.ChromeOptions()

# 2. 无界面模式
options.add_argument('--headless')

# 3. 创建参数
driver = webdriver.Chrome(options=options)

# 加载驱动
# driver = webdriver.Chrome()
# 加载网站
driver.get('https://movie.douban.com/top250')
div_tag = driver.find_element(By.XPATH, '//div[@class="hd"]')
print(div_tag.text)
