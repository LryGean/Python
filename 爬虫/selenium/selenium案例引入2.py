from selenium import webdriver
import time

driver = webdriver.Chrome()  # 加载驱动
driver.get('http://www.kuwo.cn/rankList')
time.sleep(2)
lis = driver.find_elements_by_xpath('//ul[@class="rank_list"]/li')

for i in lis:
    song_name = i.find_element_by_xpath('.//div[@class="song_name flex_c"]/a').text
    name = i.find_element_by_xpath('.//div[@class="song_artist"]/span').text
    print(song_name, name)
