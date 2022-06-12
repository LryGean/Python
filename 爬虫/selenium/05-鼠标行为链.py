from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# 加载驱动
driver = webdriver.Chrome()
# 加载网站
driver.get('https://www.baidu.com/')

input_tag = driver.find_element(By.ID, 'kw')  # 定位输入框

button_tag = driver.find_element(By.ID, 'su')  # 定位搜索按钮

# 1. 实例化对象
actions = ActionChains(driver)

# 通过行为对象调用方法
# 2. 输入内容
actions.send_keys_to_element(input_tag, 'python')
# 行为点击
actions.click(button_tag)
# 3. 执行提交
actions.perform()

# 不属于行为链里面的
# button_tag.click()
