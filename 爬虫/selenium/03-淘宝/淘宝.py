from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
import asyncio


class TBSpider:
    # 1. 初始化方法
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
        })

        # self.driver = webdriver.Chrome()
        self.driver.get('https://www.taobao.com/')
        time.sleep(1)
        # 登录
        self.pLogin = self.driver.find_element(By.CLASS_NAME, 'h')
        self.pLogin.click()
        # 输入账号
        self.driver.find_element(By.ID, 'fm-login-id').send_keys('17302254866')
        # 输入密码
        self.driver.find_element(By.ID, 'fm-login-password').send_keys('lry981222')
        time.sleep(1)
        # 点击登录
        self.driver.find_element(By.CLASS_NAME, 'password-login').click()
        time.sleep(2)
        # 输入内容
        self.driver.find_element(By.ID, 'q').send_keys('隔离')
        time.sleep(2)
        self.driver.find_element(By.ID, 'q').send_keys(Keys.ENTER)
        time.sleep(2)

    def parse_html(self):
        height = 800
        self.driver.execute_script(
            f'window.scrollTo(0, document.body.scrollHeight-{height})'
        )
        time.sleep(1)
        goods = self.driver.find_elements(By.CLASS_NAME, 'ctx-box')
        print(f'本页获取{len(goods)}个数据')
        lst = []
        for good in goods:
            try:
                item = {}
                item['价格'] = good.find_element(By.CLASS_NAME, 'price').text
                item['付款人数'] = good.find_element(By.CLASS_NAME, 'deal-cnt').text
                item['商品名'] = good.find_element(By.XPATH, './/div[@class="row row-2 title"]/a').text
                item['店铺'] = good.find_element(By.XPATH, './/div[@class="shop"]/a/span[last()]').text
                item['地点'] = good.find_element(By.XPATH, './/div[@class="row row-3 g-clearfix"]/div[@class="location"]').text
                # print(item)
                lst.append(item)
            except Exception as e:
                print(e)
            time.sleep(0.2)
        return lst

    # 存储数据
    async def saveData(self, page, lst):
        header = ('价格', '付款人数', '商品名', '店铺', '地点')
        with open(f'./data/{page}.csv', 'w', encoding='utf-8', newline='') as f:
            csvwriter = csv.DictWriter(f, header)  # 标题
            csvwriter.writeheader()  # 写入标题
            csvwriter.writerows(lst)  # 写入数据
            print(f'第{page}页下载完毕')

    async def main(self):
        tasks = []
        # 测试2页，共100页
        for i in range(0, 2):
            lst = self.parse_html()
            if self.driver.page_source.find('icon icon-btn-next-2-disable') == -1:
                self.driver.find_element(By.XPATH, '//li[@class="item next"]/a').click()
                print(lst)
                tasks.append(asyncio.create_task(self.saveData(i+1, lst)))
            else:
                self.driver.quit()
                break
        await asyncio.wait(tasks)


if __name__ == '__main__':
    t1 = time.time()
    # ID = input('请输入账号：')
    # Password = input("请输入密码：")
    # spider = TBSpider(ID, Password)
    spider = TBSpider()
    asyncio.run(spider.main())
    t2 = time.time()
    print(t2 - t1)
