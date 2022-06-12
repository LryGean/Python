# 需求：查询5月9号长沙————衡阳
import requests

url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2022-05-09&leftTicketDTO.from_station=CSQ&leftTicketDTO.to_station=HYQ&purpose_codes=ADULT"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
    'Cookie': '_uab_collina=165175594251658160859531; JSESSIONID=37BB0A7BBB9569C895359E0E0996A19F; BIGipServerotn=1206911498.50210.0000; BIGipServerpool_passport=165937674.50215.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; RAIL_EXPIRATION=1652096018672; RAIL_DEVICEID=MFnW2RZYfY_i3_Uj2kPyxyXDLnPqt_zW0QyySo0orh8xdu8D51uIWOyx3TdrxqtKmtn2KVhQrmoS8j4KS1U1MWA72bgCEZSu3ICNfKt5SO5aFEmPatv0Vj2-j7lnC48qv-upIG-WVCBE980cCWKvjH-WvoMmj5YX; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_fromStation=%u957F%u6C99%2CCSQ; _jc_save_toStation=%u8861%u9633%2CHYQ; _jc_save_fromDate=2022-05-09; _jc_save_toDate=2022-05-05; _jc_save_wfdc_flag=dc'
}

resp = requests.get(url, headers=headers)
resp.encoding = "utf-8"    # 指定编码
# print(resp.text)
# print(resp.json()['data']['result'])
result = resp.json()['data']['result']
for i in result:
    re = i.split('|')
    count = 0
    print(f'车次为{re[3]}, 二等座车票为{re[30]}, 一等座车票为{re[31]}, 商务座车票为{re[32]}')
    # for j in re:
    #     # print(count, j)
    #     count += 1
    # break

resp.close()

