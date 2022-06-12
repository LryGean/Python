import requests

url = 'https://user.qzone.qq.com/897704091'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
    'cookie': 'RK=KYnxK5TRXE; ptcz=1b9fb62aec48a75cc28339e5c136a91c52303381725b4e5b1201786e8f879cc3; pgv_pvid=1479636192; luin=o0897704091; o_cookie=897704091; pac_uid=1_897704091; qz_screen=1536x864; QZ_FE_WEBP_SUPPORT=1; tvfe_boss_uuid=fb77ed014298f6e2; eas_sid=G1S6u448J6C0E7Q216Q3m1y2L4; LW_uid=g1T644E8J6L0e7d2T6x3n1D3F7; ied_qq=o0897704091; __Q_w_s__QZN_TodoMsgCnt=1; fqm_pvqid=ffd45cb0-ecdd-4247-bd09-7a4e3a274523; LW_sid=11n6k4q8J7f7l98283P916y5R6; lskey=00010000ecc0d154c3be9d85e67725df67e2d27c35ad9730429af9b233e1dfb9ef230449fd6ff2565178e6c4; psrf_qqopenid=02AC30AE8964E95EF09245FB619007C3; tmeLoginType=2; psrf_qqaccess_token=307D1ACB9580C3493945EE96D481B156; wxunionid=; qm_keyst=Q_H_L_50p2EJ4yaDC7Y4d20N9Da4FztnPqZ8s4JIXJfqLOKqeyJw3X-uTj4sw; psrf_access_token_expiresAt=1658847581; wxopenid=; psrf_musickey_createtime=1651071581; euin=NeEl7inPoeE5; wxrefresh_token=; psrf_qqunionid=AEA9BCF11771D37825D6795BBAABB701; psrf_qqrefresh_token=DCC892A0779D5FBA10D001353BCA9F3D; _qpsvr_localtk=0.20878017305431218; uin=o0897704091; skey=@ML3DiChDL; p_uin=o0897704091; pt4_token=pP8d8UfCNAX6nkuUWJ7jPDO*ibRMMJRnLPszBw4lgOM_; p_skey=SHZsxEDkZzs10Vn4qtrI2pKiy0KkoKifGCPPTBU4K3I_; Loading=Yes; welcomeflash=897704091_83424; qqmusic_uin=0897704091; qqmusic_key=@ML3DiChDL; qqmusic_fromtag=6; pgv_info=ssid=s8518705709; qzmusicplayer=qzone_player_897704091_1651147949679; cpu_performance_v8=9'
}

response = requests.get(url, headers=headers)

print(response.text)
