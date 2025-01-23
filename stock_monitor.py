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

    'Cookie': 'cookiesu=321725805251564; device_id=69f1f5a469fccf1ee372b2db1abcbd29; smidV2=20240908222053d89f7239ebb1cbb6f1bf9e06ede5b4fc00603ec6af9a025d0; s=b216gletcb; bid=511229b42dcdeff49344a766a8e365a9_m0tnywjd; .thumbcache_f24b8bbe5a5934237bbc0eda20c1b6e7=cXCYmZVwoJ1cZ4X271XDTAcRWu20ze3bv6yt5REQtnS5zfGV6LlBF8n9QMnXc/0dMlgXYHxxOJ/24loWyN9Ddw==; acw_tc=2760826b17376470834311368eb89338c3775116885ef220a48df49e54d7c1; Hm_lvt_1db88642e346389874251b5a1eded6e3=1737647088; HMACCOUNT=743A1CF7652093E3; remember=1; xq_a_token=92395afe1963343b0b8bf2bfd7371372e8bb7d67; xqat=92395afe1963343b0b8bf2bfd7371372e8bb7d67; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjM1MzgzNzE5OTIsImlzcyI6InVjIiwiZXhwIjoxNzQwMjM5MTM5LCJjdG0iOjE3Mzc2NDcxMzkzNzMsImNpZCI6ImQ5ZDBuNEFadXAifQ.JhH4QwBkXXBvR9ojZJrq7llOmVYtAWmqtFUTzP47JIugfmGKwVqNNSkrreM0y6gKIpqivTDekodbOoDvYo6gZfgOL8FrYjW4tjW9vWkXab745TIEINsG84_MiZURrmCXpDXc8m_tFUlA2ClaCVt1POZLAOrdxVDZK-SLrhsg4vYofGsm54Tla2UpinmXDz2Pyd4vtwwnJ2RCsaqeampOino8W7ctSC4JPOHT7a2qU0XLUW6ATbyJPAE1gZPfvhvMIp36iRIyoiE70WycARlDIgoiEeGZvesNaIL1tJpDybmwCABAvc1MrFsZ1utEdcV1tCKBidZ-qjtVfV9E6jbGjw; xq_r_token=f8804a903f9c43a6e79b31fff68f4f48f839d41c; xq_is_login=1; u=3538371992; is_overseas=0; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1737647158; ssxmod_itna=Yq02DK4+O50Lx0pTlEDyDIg4jxiuc0G+R0pw43Ds3DcBDA5D8D6DQeGTtnze5i5KnSiLFfKIxaLQCWrBu2Q3WP3w3Dg7cw55oxCPGnDBFI5eCDYYCDt4DTD34DYDixib+xi5GRD0KDF+MUZBktDm4GW+qGfDDoDY3UcDitD4qDBmxQDKqGg+wwxtYt5xTbZneXQClfyDDXBD0ttxBLQIaWdEc9qDeQDtqDRDAtD8q70YUjYDIN/A2m3AihqAB3t/BiaFqGy99H/ndi2nQ4SejXqh0qaKGLs30hc5OYtt0qLwVD=Y7ofTomLCpMrDiG45lwsADDDP4rhDD===; ssxmod_itna2=Yq02DK4+O50Lx0pTlEDyDIg4jxiuc0G+R0pw4ikE5Dlp4QId08D+1YD=',

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
            # 过滤掉不需要的股票名称
            exclude_names = ['赛力斯', 'XD赛力斯']
            filtered_names = [name for name in names if name not in exclude_names]
            return filtered_names
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
