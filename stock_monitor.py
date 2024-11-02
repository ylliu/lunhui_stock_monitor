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

    'Cookie': 'cookiesu=321725805251564; device_id=69f1f5a469fccf1ee372b2db1abcbd29; smidV2=20240908222053d89f7239ebb1cbb6f1bf9e06ede5b4fc00603ec6af9a025d0; s=b216gletcb; bid=511229b42dcdeff49344a766a8e365a9_m0tnywjd; remember=1; xq_a_token=fbddae3e1ced0f777e9a6531312c6a1de23a8650; xqat=fbddae3e1ced0f777e9a6531312c6a1de23a8650; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjM1MzgzNzE5OTIsImlzcyI6InVjIiwiZXhwIjoxNzMzMTEzNTc0LCJjdG0iOjE3MzA1MjE1NzQzNTYsImNpZCI6ImQ5ZDBuNEFadXAifQ.DCNo5A-nQufno_4pygqqskbm5L-OtHuF6_8EXl96JY_56d7Megtqj0RGpUvz9joga5EeeVp32ZHbV6R7tU8OmHjGDSGFndxT8k28gFSno3ASRJUINd64oScRrAeSIS7nnVgdFyniqdfNOz422CphzEono9zGSGHhIDsIPiNjByeyAXVA7eb-Gw5q2uo8iiLQb7zwSFnv5dVYtGFkqkiGNOTdbCuB4qbycTJrDxN-yxHE6aMCoLG_0hhlxhXAe7LPgjb6E1cfhBGkv6AotZLubsNsfQyLfpsfFFcyI0v1b0S4_lRBSxviUVnUPOYcqrGUta7OuwFA_5Rgb-kmFCnBAw; xq_r_token=eadf667fbcdb84323e28c14ae3a18cfcc3fe4d61; xq_is_login=1; u=3538371992; acw_tc=2760826a17305478574165555ebde749dba8ff0014f7fdd473aeb7a6b63714; is_overseas=0; Hm_lvt_1db88642e346389874251b5a1eded6e3=1730547859; HMACCOUNT=743A1CF7652093E3; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1730547872; .thumbcache_f24b8bbe5a5934237bbc0eda20c1b6e7=cXCYmZVwoJ1cZ4X271XDTAcRWu20ze3bv6yt5REQtnS5zfGV6LlBF8n9QMnXc/0dMlgXYHxxOJ/24loWyN9Ddw==; ssxmod_itna=7qGx2i0=eiTxzxmxB4OKsIe7K4AKIeDCbQ7+YzePuDBu0MxiNDnD8x7YDvzjOeTh3+vNz8rCTKNkKnbnDKXF9Qrm=6DmucWoxCPGnDB9KQjDemtD5xGoDPxDeDADYE0DAqiOD7qDdXLvvz2xGWDmRkDWPDYxDrXpKDRxi7DD5=sx07DQykqGRkQ/PmBhE1k0YF6xDzXxG1840HkDdxXrOjubGssx0ODiKDcxik//p0m=hXSEv=rm0PFGGP7=DWP9b8DlF9lf5zVPKITY5GMaAerPxqNeedEqqxP0DcN0G4kYRbeC0qahPFuTehYqjwGeDDipDjlGxlG=YD==; ssxmod_itna2=7qGx2i0=eiTxzxmxB4OKsIe7K4AKIeDCbQ7+YzePx8wPreGNNGCKDFxp/Kt97MKGFQmw2Ksqlmw7+I2KRw5vvDoUg70fy9egEACkOln0UYhsKhYw61uRlCFG3yYt7eCIX+z=xBkbYWz71piDfHF3PntnrpOqcyhM75kA1TstlmbZxR7exO1Blg7r=D=W1u8k7ipE9KrggrQD6ExLKhIkO3qp6cfYDWf+o+O+tjpv208O19Kb/PwBQowxPS=zi0Ttech80MK2te=Dfmrz6uuq8F0w9vTdqEQ33eiQ95WHMulQ5BF5=LWcR5lOd7d4D43TuYx4iIY4I3YMbYrmx7TzqgOoYK9k=V3Kt+Yn0WBRh275iRH323I4NZRwrh+R8kLRmkOD2DiZ2DrAd3q7Q7axxvy7PgManBY41q9Q4odQlB3aWa5LONhKehQW3Y+YpKf+oh503kwkdOntBGzaePGrawhIVgWZhKajFTPASCfnGPD7j1+4sCEYlpYl6CjTjryTY74NjVbiGQB1WdVbytlBI=WThDzC+CivkQDtCeS90tXK8Y4DjKDeqkhGx2bekiDD',

    'origin': 'https://xueqiu.com',
    'Referer': 'https://xueqiu.com/u/8282709675',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 SE 2.X MetaSr 1.0',
    'X-Requested-With': 'XMLHttpRequest'
}

# urllib 的相关操作如下
url = 'https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json?pid=-1&category=1&size=1000&uid=8282709675'


# url = 'https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json?pid=-1&category=1&size=1000&uid=3538371992'


# 获取股票基础信息

class StockMonitor:
    def get_self_stocks(self):
        try:
            response = requests.get(url, headers=headers)
            data = json.loads(response.text)
            # 从解析后的字典中提取stocks列表
            stocks = data['data']['stocks']
            names = [stock['name'] for stock in stocks]
            return names
        except Exception as e:
            return response.text

    def send_message(self, add_stocks, remove_stocks):
        if len(add_stocks) == 0 and len(remove_stocks) == 0:
            return
            # 你的Server酱API密钥
        SCKEY = 'SCT205498TVznAyJOnylNd4bE42tWSz3mp'

        # 发送消息到钉钉的URL
        url = f'https://sctapi.ftqq.com/{SCKEY}.send?channel=2'

        # 要发送的消息内容，你可以根据Server酱的文档来格式化这个JSON
        # 这里只是一个简单的示例
        data = {
            "text": f"新增:{add_stocks},移除:{remove_stocks}",
            "desp": f"新增:{add_stocks},移除:{remove_stocks}"
        }

        # 发送POST请求
        response = requests.post(url, data=data)

        # 打印响应结果，检查是否发送成功
        print(response.text)

    def get_add_stocks(self, stocks, previous):
        return [stock for stock in stocks if stock not in previous]

    def get_remove_stocks(self, stocks, previous):
        return [stock for stock in previous if stock not in stocks]

    def send_message2(self, title, content):
        SCKEY = 'SCT205498TVznAyJOnylNd4bE42tWSz3mp'

        # 发送消息到钉钉的URL
        url = f'https://sctapi.ftqq.com/{SCKEY}.send?channel=2'

        # 要发送的消息内容，你可以根据Server酱的文档来格式化这个JSON
        # 这里只是一个简单的示例
        data = {
            "text": f"{title}",
            "desp": f"{content}"
        }

        # 发送POST请求
        response = requests.post(url, data=data)

    def send_message2_wechat(self, title, content):
        SCKEY = 'SCT205498TVznAyJOnylNd4bE42tWSz3mp'

        # 发送消息到钉钉的URL
        url = f'https://sctapi.ftqq.com/{SCKEY}.send?channel=9'

        # 要发送的消息内容，你可以根据Server酱的文档来格式化这个JSON
        # 这里只是一个简单的示例
        data = {
            "text": f"{title}",
            "desp": f"{content}"
        }

        # 发送POST请求
        response = requests.post(url, data=data)

    def send_message_to_wechat(self, add_stocks, remove_stocks):
        if len(add_stocks) == 0 and len(remove_stocks) == 0:
            return
            # 你的Server酱API密钥
        SCKEY = 'SCT205498TVznAyJOnylNd4bE42tWSz3mp'

        # 发送消息到钉钉的URL
        url = f'https://sctapi.ftqq.com/{SCKEY}.send?channel=9'

        # 要发送的消息内容，你可以根据Server酱的文档来格式化这个JSON
        # 这里只是一个简单的示例
        data = {
            "text": f"new stock coming",
            "desp": f"新增:{add_stocks},移除:{remove_stocks}"
        }

        # 发送POST请求
        response = requests.post(url, data=data)

        # 打印响应结果，检查是否发送成功
        print(response.text)
