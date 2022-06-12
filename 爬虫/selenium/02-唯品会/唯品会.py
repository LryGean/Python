from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
import asyncio


class WPHSpider:
    # 1. 初始化方法
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.vip.com/')
        # 输入内容
        self.driver.find_element(By.CLASS_NAME, 'c-search-input').send_keys('苹果')
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, 'c-search-input').send_keys(Keys.ENTER)
        time.sleep(2)

    def parse_html(self):
        # 页面拉至低端
        scroll = 1000
        height = 500
        while True:
            hights = self.driver.execute_script('return document.documentElement.scrollTop')
            print(hights, height)
            if height != hights:
                self.driver.execute_script(
                    f'window.scrollTo(0, {scroll})'
                )
                height = hights
                # print(scroll)
                scroll += 500
                time.sleep(0.5)
            else:
                goods = self.driver.find_elements(By.XPATH, '//section[@id="J_searchCatList"]/div[@class="c-goods-item  J-goods-item c-goods-item--auto-width"]/a//div[@class="c-goods-item-bottom    "]')
                print(f'本页获取{len(goods)}个数据')
                lst = []
                for good in goods:
                    try:
                        item = {}
                        main_price = good.find_elements(By.XPATH, './/div[@class="c-goods-item__main-price     J-goods-item__main-price"]/div')
                        # 售价为小数，有折扣
                        if len(main_price) == 5:
                            # 售价
                            item['售价'] = good.find_element(By.CLASS_NAME, 'c-goods-item__sale-price').text + main_price[2].text
                            # 原价
                            item['原价'] = good.find_element(By.CLASS_NAME, 'J-goods-item__market-price').text
                            item['折扣'] = good.find_element(By.CLASS_NAME, 'c-goods-item__discount').text
                        # 售价为整数，有折扣
                        elif len(main_price) == 4:
                            # 售价
                            item['售价'] = good.find_element(By.CLASS_NAME, 'c-goods-item__sale-price').text
                            # 原价
                            item['原价'] = good.find_element(By.CLASS_NAME, 'J-goods-item__market-price').text
                            item['折扣'] = good.find_element(By.CLASS_NAME, 'c-goods-item__discount').text
                        # 无折扣
                        elif len(main_price) == 1:
                            # 售价
                            item['售价'] = good.find_element(By.CLASS_NAME, 'c-goods-item__sale-price').text
                            # 原价
                            item['原价'] = good.find_element(By.CLASS_NAME, 'c-goods-item__sale-price').text
                            item['折扣'] = '无折扣'
                        # 商品名
                        item['商品名'] = good.find_element(By.CLASS_NAME, 'c-goods-item__name').text
                        # print(item)
                        lst.append(item)
                    except Exception as e:
                        print(e)
                break
            time.sleep(0.2)
        return lst

    # 存储数据
    async def saveData(self, page, lst):
        header = ('售价', '原价', '折扣', '商品名')
        with open(f'./data/{page}.csv', 'w', encoding='utf-8', newline='') as f:
            csvwriter = csv.DictWriter(f, header)  # 标题
            csvwriter.writeheader()  # 写入标题
            csvwriter.writerows(lst)  # 写入数据
            print(f'第{page}页下载完毕')

    # 主函数
    async def main(self):
        tasks = []
        # 测试2页，总共12页
        for i in range(0, 2):
            lst = self.parse_html()
            if self.driver.page_source.find('cat-paging-next'):
                self.driver.find_element(By.CLASS_NAME, 'cat-paging-next').click()
                time.sleep(0.5)
                print(lst)
                tasks.append(asyncio.create_task(self.saveData(i+1, lst)))
                # self.saveData(i+1, lst)
            else:
                self.driver.quit()
                break
        await asyncio.wait(tasks)
        print(len(tasks))


if __name__ == '__main__':
    t1 = time.time()
    spider = WPHSpider()
    asyncio.run(spider.main())
    t2 = time.time()
    print(t2-t1)
