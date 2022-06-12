# 目标：购买郑州到天津的车票

from selenium import webdriver
from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
import time
import csv
import asyncio


class RailWaySpider:
    def __init__(self):
        # 反爬
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 加载驱动
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
        })
        # 加载网站
        self.driver.get('https://www.12306.cn/index/index.html')
        self.driver.implicitly_wait(1)

    # 登录
    def Login(self):
        self.driver.find_element(By.ID, 'J-btn-login').click()
        self.driver.implicitly_wait(1)
        # 账号
        self.driver.find_element(By.ID, 'J-userName').send_keys('17302254866')
        # 密码
        self.driver.find_element(By.ID, 'J-password').send_keys('lry1730225')
        # 登录
        self.driver.find_element(By.ID, 'J-login').click()
        # 滑块位置
        block = self.driver.find_element(By.ID, 'nc_1_n1z')
        # 实例化对象
        action = ActionChains(self.driver)
        # 鼠标左键按下不放
        action.click_and_hold(block).perform()
        # 移动鼠标
        try:
            action.drag_and_drop_by_offset(block, 300, 0).perform()
        except UnexpectedAlertPresentException:
            print('验证失败')
        if self.driver.page_source.find('nc_1_refresh1'):
            self.driver.find_element(By.ID, 'nc_1_refresh1').click()
            time.sleep(2)
            # 滑块位置
            block = self.driver.find_element(By.ID, 'nc_1_n1z')
            # 鼠标左键按下不放
            action.click_and_hold(block).perform()
            # 移动鼠标
            try:
                action.drag_and_drop_by_offset(block, 300, 0).perform()
            except UnexpectedAlertPresentException:
                print('验证失败')
        # 确定
        self.driver.find_element(By.CLASS_NAME, 'ok').click()
        # 进入主页
        self.driver.find_element(By.CLASS_NAME, 'nav-hd').click()
        self.driver.implicitly_wait(1)

    def Search(self):
        # 选择出发地
        start = self.driver.find_element(By.ID, 'fromStationText')
        start.click()
        # 郑州
        self.driver.find_element(By.XPATH, '//ul[@class="popcitylist"]/li[last()-2]').click()
        # 选择到达地
        to = self.driver.find_element(By.ID, 'toStationText')
        to.click()
        # 天津
        self.driver.find_element(By.XPATH, '//ul[@class="popcitylist"]/li[3]').click()
        # 选择出发时间
        sdate = self.driver.find_element(By.ID, 'train_date')
        # sdate.click()
        sdate.clear()
        sdate.send_keys('2022-06-18')
        # 选择学生
        student = self.driver.find_element(By.XPATH, '//li[@id="isStudentDan"]/i')
        self.driver.execute_script('arguments[0].click();', student)
        # 点击查询
        self.driver.find_element(By.ID, 'search_one').click()
        self.driver.implicitly_wait(1)

    def Reserve(self):
        # 切换窗口
        self.driver.switch_to.window(self.driver.window_handles[1])
        # print(self.driver.current_url)  # 当前页面的url
        # 预定K126车次
        ticket = self.driver.find_element(By.XPATH, '//tr[@id="ticket_410000K12631_04_13"]/td[@class="no-br"]/a[@class="btn72"]')
        self.driver.execute_script('arguments[0].click();', ticket)
        time.sleep(1)
        # print(self.driver.current_url)  # 当前页面的url
        # 确认乘客
        me = self.driver.find_element(By.XPATH, '//ul[@id="normal_passenger_id"]/li[1]/input')
        self.driver.execute_script('arguments[0].click();', me)
        time.sleep(1)
        ok = self.driver.find_element(By.ID, 'dialog_xsertcj_ok')
        self.driver.execute_script('arguments[0].click();', ok)
        time.sleep(1)
        # 提交订单
        form = self.driver.find_element(By.ID, 'submitOrder_id')
        self.driver.execute_script('arguments[0].click();', form)
        self.driver.implicitly_wait(1)
        # 确认
        self.driver.find_element(By.ID, 'qr_submit_id').click()

    def main(self):
        self.Login()
        self.Search()
        self.Reserve()


if __name__ == '__main__':
    t1 = time.time()
    spider = RailWaySpider()
    spider.main()
    t2 = time.time()
    print(t2 - t1)
