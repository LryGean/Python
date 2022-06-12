from selenium import webdriver
from selenium.webdriver.common.by import By
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

# # 加载驱动
# driver = webdriver.Chrome()
# 加载网站
driver.get('https://www.douban.com/')
time.sleep(2)

# 若页面中有iframe标签，得先切入iframe标签
login_frame = driver.find_element(By.XPATH, '//div[@class="login"]/iframe')
driver.switch_to.frame(login_frame)
# 点击密码登录
driver.find_element(By.CLASS_NAME, 'account-tab-account').click()
# 输入账号密码
driver.find_element(By.ID, 'username').send_keys('17302254866')
driver.find_element(By.ID, 'password').send_keys('lry1730225')

# driver.find_element(By.CLASS_NAME, 'btn-account').click()
driver.find_element(By.XPATH, '//div[@class="account-form-field-submit "]/a').click()
