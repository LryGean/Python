from selenium import webdriver
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(chrome_options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

# driver = webdriver.Chrome()
driver.get('https://www.wjx.cn/jq/87910206.aspx')
time.sleep(2)

questions = driver.find_elements(By.CLASS_NAME, 'div_question')

'''
    对题目进行分类
    单选：1-10
    多选：11-12
'''
one_choice = [0, 1, 2, 3, 4, 5, 6, 8, 9]
any_choice = [10, 11]
# 解决单选循环：10次
for i in one_choice:
    lis = questions[i].find_elements(By.XPATH, '//ul[@class="ulradiocheck"]/li')
    # 随机取其中一个li进行点击
    random.choice(lis).click()

# 多选
for j in any_choice:
    # 返回的是列表类型；通过len函数
    # 元素都是存放在lis里面
    lis = questions[j].find_elements(By.XPATH, '//ul[@class="ulradiocheck"]/li')
    num = random.randint(1, len(lis))  # 全闭区间， 在范围内随机生成一个数
    # lis当中抽取num个元素
    lst = random.sample(lis, num)   # 随机取样， 列表
    for k in lst:
        k.click()

time.sleep(2)

driver.find_element(By.ID, 'submit_button').click()

time.sleep(2)
driver.find_element(By.ID, 'rectTop').click()
time.sleep(2)
driver.find_element(By.ID, 'submit_button').click()
