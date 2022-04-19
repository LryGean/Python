# 1.拿到主页面的源代码，然后提取到子页面的链接地址，href
# 2.通过href拿到子页面的内容，从子页面中找到图片的下载地址 img ——> src
# 3.下载链接
import requests
from bs4 import BeautifulSoup
import time


url = 'https://www.umeitu.com/bizhitupian/weimeibizhi/'
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
}

resp = requests.get(url, headers=header)
resp.encoding = 'utf-8'
# print(resp.text)
# 把源代码交给bs
main_page = BeautifulSoup(resp.text, "html.parser")
a_list = main_page.find('ul', class_="pic-list after").find_all("a")    # 把范围第一次缩小
# print(a_list)

for a in a_list:
    # ********************************************************************
    href = f"https://www.umeitu.com{a.get('href')}"  # 直接通过get拿到属性值
    # ********************************************************************
    # 拿到子页面的源代码
    child_page_resp = requests.get(href)
    child_page_resp.encoding = "utf-8"
    child_page_text = child_page_resp.text
    # 从子页面中拿到图片下载地址
    child_page = BeautifulSoup(child_page_text, "html.parser")
    section = child_page.find("section", class_="img-content")
    # print(section)
    img = section.find('img')
    # print(img)
    # *******************
    src = img.get('src')
    # *******************
    # 下载图片
    img_resp = requests.get(src)
    # img_resp.content()       # 这里拿到的是字节

    # .text:表示拿到被标签标记的内容
    main_bt = child_page.find('div', class_="main-bt")
    title = main_bt.find('h1').text
    with open(f'./唯美壁纸/{title}.jpg', 'wb') as f:
        f.write(img_resp.content)    # 图片内容写入文件
    child_page_resp.close()
    print("over!", title)
    f.close()
    time.sleep(1)           # 为了防止服务器不限制访问次数，下载完一张图片进行睡眠

print('all over!!!')

resp.close()
