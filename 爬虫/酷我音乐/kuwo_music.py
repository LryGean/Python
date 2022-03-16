from urllib.parse import urlencode
import json
import requests



class Kuwo_Music(object):
    def __init__(self):
        self.music_data_url = "http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?"
        self.data_list_url = "http://www.kuwo.cn/api/v1/www/music/playUrl?"
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Cookie": "_ga=GA1.2.1127884270.1628076200; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1647433235; _gid=GA1.2.773811496.1647433235; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1647434121; kw_token=S8LQE81FEX",
            "csrf": "S8LQE81FEX",
            "Host": "www.kuwo.cn",
            "Referer": "http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
        }


    def get_rid_index(self,rid,name,artist):
        data = {
            "mid": rid,
            "type": "convert_url3",
            "httpsStatus": "1",
            "reqId": "8b457241 - a525 - 11ec - 8182 - 0d633f56a64e"
        }
        data_url = self.data_list_url+urlencode(data)
        response = requests.get(url=data_url,headers=self.headers).text
        music_url = json.loads(response)["data"]["url"]
        self.write_data(music_url,name)
        print("正在保存----",name)

    def get_page_index(self,name,num):
        params = {
            "key":name,
            "pn":num,
            "rn":"30",
            "httpsStatus":"1",
            "reqId":"8b44aef0 - a525 - 11ec - 8182 - 0d633f56a64e"
        }
        data_url = self.music_data_url+urlencode(params)
        response = requests.get(url=data_url,headers=self.headers).text
        json_data = json.loads(response)["data"]["list"]
        for data in json_data:
            name = data["name"]
            artist = data["artist"]
            rid = data["rid"]
            self.get_rid_index(rid,name,artist)


    def write_data(self,music_url,name):
        with open("./周杰伦/"+name+".mp3","ab") as f:
            resp = requests.get(music_url).content
            f.write(resp)

    def run(self):
        name=input("输入歌手")
        num = input("输入页数")
        self.get_page_index(name,num)


if __name__ == '__main__':
    spider = Kuwo_Music()
    spider.run()