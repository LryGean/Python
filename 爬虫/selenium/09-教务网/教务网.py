from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
import time
import csv
import asyncio


class JWWSpider:
    def __init__(self):
        # 反爬
        self.options = webdriver.ChromeOptions()

        # self.proxy_ip = ""
        # proxy = "--proxy-server=http://" + self.proxy_ip
        # self.options.add_argument(proxy)

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
        self.driver.get('http://61.181.145.1:89/jsxsd/')
        time.sleep(3)

    def Login(self):
        self.driver.find_element(By.ID, 'userAccount').send_keys('195150118')
        self.driver.find_element(By.ID, 'userPassword').send_keys('lry981222')
        self.driver.find_element(By.ID, 'RANDOMCODE').click()
        time.sleep(5)
        # 等待输入验证码
        self.driver.find_element(By.ID, 'RANDOMCODE').send_keys(Keys.ENTER)
        # self.driver.find_element(By.CLASS_NAME, 'login_btn').click()

    def UserInfo(self):
        # 切入iframe标签
        iframe = self.driver.find_element(By.ID, 'Frame0')
        self.driver.switch_to.frame(iframe)
        lis = self.driver.find_elements(By.XPATH, '//div[@class="middletopttxlr"]/div')[1:]
        print(f'获取{len(lis)}条')
        lst = []
        item = {}
        for info in lis:
            try:
                key = info.find_element(By.CLASS_NAME, 'middletopdwxxtit').text.strip('：')
                value = info.find_element(By.CLASS_NAME, 'middletopdwxxcont').text
                item[key] = value
                # print(item)
            except Exception as e:
                print(e)
            time.sleep(0.2)
        lst.append(item)
        print(lst)
        return lst

    async def CourseGrade(self):
        # self.driver.find_elements(By.XPATH, '//div[@class="panel-body"]/div[@class="cy_icon"]/div[@class="grid"]')[1].click()
        # time.sleep(1)
        try:
            self.driver.find_elements(By.XPATH, '//div[@class="panel-body"]/div[@class="cy_icon"]/div[@class="grid"]')[1].click()
            time.sleep(1)
        except Exception as e:
            print('出错了')
            print(e)
            self.driver.find_elements(By.XPATH, '//div[@class="panel-body"]/div[@class="cy_icon"]/div[@class="grid"]')[1].click()
            time.sleep(1)
        # # 切换页面
        # self.driver.switch_to.window(self.driver.window_handles[0])
        # time.sleep(1)
        # 切回来
        self.driver.switch_to.default_content()
        # 切入iframe1标签
        iframe1 = self.driver.find_element(By.ID, 'Frame1')
        self.driver.switch_to.frame(iframe1)

        # 切入iframe2标签
        iframe2 = self.driver.find_element(By.ID, 'cjcx_query_frm')
        self.driver.switch_to.frame(iframe2)

        select_tag = Select(self.driver.find_element(By.ID, 'kksj'))
        tasks = []
        for i in range(3, 8):
            select_tag.select_by_index(i)
            self.driver.find_element(By.ID, 'btn_query').click()

            # 切回来
            self.driver.switch_to.default_content()
            # 切入iframe1标签
            iframe1 = self.driver.find_element(By.ID, 'Frame1')
            self.driver.switch_to.frame(iframe1)
            # 切入iframe3标签
            iframe3 = self.driver.find_element(By.ID, 'cjcx_list_frm')
            self.driver.switch_to.frame(iframe3)

            trs = self.driver.find_elements(By.XPATH, '//table[@id="dataList"]//tr')
            print(f'共有{len(trs)}节课')
            lst = []
            for j in range(len(trs)):
                if j == 0:
                    ths = trs[j].find_elements(By.XPATH, './/th')
                    th_lst = []
                    for th in ths:
                        th_lst.append(th.text)
                    # print(th_lst)
                else:
                    tds = trs[j].find_elements(By.XPATH, './/td')
                    item = {}
                    for t in range(len(tds)):
                        item[th_lst[t]] = tds[t].text
                    lst.append(item)
            # print(lst)
            tasks.append(asyncio.create_task(self.saveCourse(lst, tuple(th_lst))))

            # 切回来
            self.driver.switch_to.default_content()
            # 切入iframe1标签
            iframe1 = self.driver.find_element(By.ID, 'Frame1')
            self.driver.switch_to.frame(iframe1)
            # 切入iframe2标签
            iframe2 = self.driver.find_element(By.ID, 'cjcx_query_frm')
            self.driver.switch_to.frame(iframe2)
            time.sleep(0.2)
        await asyncio.wait(tasks)

    async def saveCourse(self, lst, header):
        with open(f'./Data/Courses/{lst[0]["开课学期"]}.csv', 'w', encoding='utf-8', newline='') as f:
            csvwriter = csv.DictWriter(f, header)  # 标题
            csvwriter.writeheader()  # 写入标题
            csvwriter.writerows(lst)  # 写入数据
            print(f'{lst[0]["开课学期"]}下载完毕')
            f.close()

    def saveInfo(self, lst):
        header = ('学生姓名', '学生编号', '所属院系', '专业名称', '班级名称')
        with open('./Data/info.csv', 'w', encoding='utf-8', newline='') as f:
            csvwriter = csv.DictWriter(f, header)  # 标题
            csvwriter.writeheader()  # 写入标题
            csvwriter.writerows(lst)  # 写入数据
            f.close()

    def main(self):
        # 登录
        self.Login()
        lst = self.UserInfo()
        self.saveInfo(lst)
        asyncio.run(self.CourseGrade())


if __name__ == '__main__':
    t1 = time.time()
    spider = JWWSpider()
    # asyncio.run(spider.main())
    spider.main()
    t2 = time.time()
    print(t2 - t1)


