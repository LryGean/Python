from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv


class JDSpider:

    lst = []    #

    # 1. 初始化方法
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.jd.com/')
        # 输入内容
        self.driver.find_element(By.ID, 'key').send_keys('爬虫书')
        time.sleep(1)
        self.driver.find_element(By.ID, 'key').send_keys(Keys.ENTER)
        time.sleep(2)

    # 2. 解析数据
    def parse_html(self):
        self.driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight)'
        )
        time.sleep(3)
        lists = self.driver.find_elements(By.XPATH, '//div[@id="J_goodsList"]/ul/li')

        for li in lists:
            try:
                item = {}
                # 价格
                item['price'] = li.find_element(By.XPATH, './/div[@class="p-price"]/strong').text
                # 书名
                item['name'] = li.find_element(By.XPATH, './/div[@class="p-name"]/a/em').text
                # 评价条数
                item['commit'] = li.find_element(By.XPATH, './/div[@class="p-commit"]/strong').text
                # 店铺
                item['shop'] = li.find_element(By.XPATH, './/div[@class="p-shopnum"]/a').text
                print(item)
                self.lst.append(item)
            except Exception as e:
                print(e)

    # 3. 存储数据
    def save_data(self):
        with open('./Data/京东爬虫书籍.csv', 'w', encoding='utf-8', newline='') as f:
            csvwriter = csv.DictWriter(f, fieldnames=['price', 'name', 'commit', 'shop'])
            csvwriter.writeheader()
            csvwriter.writerows(self.lst)

    # 主函数
    def main(self):
        for i in range(1, 5):
            self.parse_html()
            if self.driver.page_source.find('pn-next disabled') == -1:
                self.driver.find_element(By.CLASS_NAME, 'pn-next').click()
                time.sleep(2)
            else:
                self.driver.quit()
                break
        self.save_data()


if __name__ == '__main__':
    spider = JDSpider()
    spider.main()
