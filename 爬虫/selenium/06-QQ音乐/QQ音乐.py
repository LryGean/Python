from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
import time


class QQSpider:
    # 初始化方法
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
        self.driver.get('https://y.qq.com/')
        time.sleep(1)
        # 登录
        self.driver.find_element(By.CLASS_NAME, 'top_login__link').click()
        time.sleep(1)
        # 切入iframe标签
        self.iframe1 = self.driver.find_element(By.ID, 'login_frame')
        self.driver.switch_to.frame(self.iframe1)
        self.iframe2 = self.driver.find_element(By.ID, 'ptlogin_iframe')
        self.driver.switch_to.frame(self.iframe2)
        self.driver.find_element(By.ID, 'switcher_plogin').click()

    def Login(self):
        # 账号
        self.driver.find_element(By.ID, 'u').send_keys('89770491')
        # 密码
        self.driver.find_element(By.ID, 'p').send_keys('Lry17302254866')
        time.sleep(1)
        self.driver.find_element(By.ID, 'login_button').click()
        self.driver.maximize_window()
        time.sleep(2)

    def Search(self):
        # 切回来
        self.driver.switch_to.default_content()
        # 实例化对象
        actions = ActionChains(self.driver)
        # 搜索框的位置
        searchbutton = self.driver.find_element(By.CLASS_NAME, 'search_input__btn')
        # 移动操作
        actions.move_to_element(searchbutton)
        time.sleep(1)
        # 提交
        actions.perform()
        search = self.driver.find_element(By.CLASS_NAME, 'search_input__input')
        search.send_keys('再次爱上你')
        search.send_keys(Keys.ENTER)

    def Click(self):
        actions = ActionChains(self.driver)
        song = self.driver.find_element(By.XPATH, '//div[@class="mod_songlist "]/ul[@class="songlist__list"]/li[1]')
        # 移动操作
        actions.move_to_element(song)
        time.sleep(1)
        # 提交
        actions.perform()
        # 执行js代码进行点击
        ele = song.find_element(By.XPATH, '//div[@class="mod_list_menu"]/a[@class="list_menu__item list_menu__play"]')
        ele.click()
        # self.driver.execute_script("arguments[0].click()", ele)
        time.sleep(3)
        # 切换窗口
        self.driver.switch_to.window(self.driver.window_handles[1])
        print(self.driver.current_url)  # 当前页面的url
        time.sleep(2)
        lastbutton = self.driver.find_element(By.CLASS_NAME, 'upload_btns__item')
        lastbutton.click()

    def main(self):
        self.Login()
        time.sleep(2)
        self.Search()
        time.sleep(3)
        self.Click()


if __name__ == '__main__':
    t1 = time.time()
    spider = QQSpider()
    spider.main()
    t2 = time.time()
    print(t2-t1)


