import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['qq.com']
    start_urls = ['https://user.qzone.qq.com/897704091']

    def start_requests(self):
        cookies = 'RK=2Yn5ObTBTk; ptcz=79b3bcf25b215e1505554e3275615138e4fa39d98c92601fe60cf45ebef26e27; pgv_pvid=8780614736; qz_screen=1536x864; QZ_FE_WEBP_SUPPORT=1; __Q_w_s_hat_seed=1; __Q_w_s__QZN_TodoMsgCnt=1; luin=o0897704091; lskey=00010000c0c9a345591bef8bead6f1f11a687f916fac1b84b1afccde5ea86d013d3ae2ea3611800adbf8f349; pgv_info=ssid=s8552293878; zzpaneluin=; zzpanelkey=; _qpsvr_localtk=0.47279971218456796; uin=o0897704091; skey=@7xU9wwZsp; p_uin=o0897704091; Loading=Yes; qqmusic_uin=0897704091; qqmusic_key=@7xU9wwZsp; qqmusic_fromtag=6; welcomeflash=897704091_83424; pt4_token=EFoMblQ4J31mkOSGv9JWnUK*fmSLE5eXMxN07XIyZA8_; p_skey=6V7XDvb2QgXsWh39gq7BAaDnVBc89mRvJpzmqMuaxAw_; qzmusicplayer=qzone_player_897704091_1656603257412; cpu_performance_v8=3'

        cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies.split(';')}

        yield scrapy.Request(url=self.start_urls[0], callback=self.parse, cookies=cookies)

    def parse(self, response):
        with open('qzone.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
