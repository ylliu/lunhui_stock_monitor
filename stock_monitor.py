import json
import time
import requests

# 因为不能访问, 所以我们加个头试试
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'cookiesu=321725805251564; device_id=69f1f5a469fccf1ee372b2db1abcbd29; remember=1; xq_a_token=76b972107860206e818a9e1f4135aa19b83de462; xqat=76b972107860206e818a9e1f4135aa19b83de462; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjM1MzgzNzE5OTIsImlzcyI6InVjIiwiZXhwIjoxNzI4MDM0OTg3LCJjdG0iOjE3MjU4MDUzNjA0NzgsImNpZCI6ImQ5ZDBuNEFadXAifQ.aBJTlApCut0tT10_jGlh7XnVpjlH0u5TDXZ3I1IYloGIuwis2JtDB9P18LWKTX9ZOJIJlNQ6tGpRLMwQb7C-BEdOzqtIbc7eH4CLzxVjU5SPKP404tDBIaOkD5eaDxHDcyiMxCDqLssSaOAX4n2LtsBiPnUtJ_Zt4Lf5O_KRtR2ukGOWsSZeOwWGpA1WoKaRmdL6g71_KjM8D_Y0jKbGWy3JZLPIZfuq3UwJEEQ0aJsk486ri-y-HvxPbCewAdDWbLdtMRH8F1kB9ucK0LAA6vv_zSSm8cokWtT92SRdzp_CH4OTN1H-3zy3eKs3FVz4jSWzFJmJs9pkk0oNH7wz6Q; xq_r_token=5bfe95f8eff0e079426483b83d329fe8b08e3219; xq_is_login=1; u=3538371992; s=b216gletcb; bid=511229b42dcdeff49344a766a8e365a9_m0tnywjd; snbim_minify=true; Hm_lvt_1db88642e346389874251b5a1eded6e3=1725807000; HMACCOUNT=743A1CF7652093E3; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1725807077; ssxmod_itna=YqUhD54fxRrdGHqGdD7IqYYKRi1fSfnfDjrOkqGN=WDZDiqAPGhDC4bKGKiE3X33WAbrPDujrh2bftWb52xaWa+hKaQQff4e4iDCPGnDBI2Q5GDYYkDt4DTD34DYDixibwxi5GRD0KDFmqN/SwtDm4GWmqGfDDoDYbt9DitD4qDBGoQDKqGgmLeEmM20ICX=uuA5ODtD0TtDjLTD/RAOLiUdEc934QQDtqDRDAtD8dB039jo4UX/mEDQUGmd7AmviWP9DB66V6XZeCj=vAUxZqroG8D1GGLxikZFQE41jK4142AqWf+rS8DQGx9MDS0d801EiqDD3U0P=YD=; ssxmod_itna2=YqUhD54fxRrdGHqGdD7IqYYKRi1fSfnfDjrOqA6n3D/bxKuP7=D2feD=',
    'origin': 'https://xueqiu.com',
    'Referer': 'https://xueqiu.com/u/8282709675',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 SE 2.X MetaSr 1.0',
    'X-Requested-With': 'XMLHttpRequest'
}

# urllib 的相关操作如下
url = 'https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json?pid=-1&category=1&size=1000&uid=8282709675'


# 获取股票基础信息

class StockMonitor:
    def get_self_stocks(self):
        # print(url.format(symbol=stock_symbol,timestamp=timestp))
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        # 从解析后的字典中提取stocks列表
        stocks = data['data']['stocks']
        return stocks

    def send_message(self, add_stocks, remove_stocks):
        # 你的Server酱API密钥
        SCKEY = 'SCT205498TVznAyJOnylNd4bE42tWSz3mp'

        # 发送消息到钉钉的URL
        url = f'https://sctapi.ftqq.com/{SCKEY}.send?channel=2'

        # 要发送的消息内容，你可以根据Server酱的文档来格式化这个JSON
        # 这里只是一个简单的示例
        data = {
            "text": f"新增:{add_stocks},移除:{remove_stocks}"
        }

        # 发送POST请求
        response = requests.post(url, data=data)

        # 打印响应结果，检查是否发送成功
        print(response.text)
