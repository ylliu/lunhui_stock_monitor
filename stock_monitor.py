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

    'Cookie': 'cookiesu=321725805251564; device_id=69f1f5a469fccf1ee372b2db1abcbd29; smidV2=20240908222053d89f7239ebb1cbb6f1bf9e06ede5b4fc00603ec6af9a025d0; s=b216gletcb; bid=511229b42dcdeff49344a766a8e365a9_m0tnywjd; .thumbcache_f24b8bbe5a5934237bbc0eda20c1b6e7=cXCYmZVwoJ1cZ4X271XDTAcRWu20ze3bv6yt5REQtnS5zfGV6LlBF8n9QMnXc/0dMlgXYHxxOJ/24loWyN9Ddw==; acw_tc=1a0c66d617350537281103459e0148c1db3977398551b4d8a0c132098845fc; Hm_lvt_1db88642e346389874251b5a1eded6e3=1735053733; HMACCOUNT=743A1CF7652093E3; remember=1; xq_a_token=818e78e808c5fc9082ab70c8e30ff3985f918d60; xqat=818e78e808c5fc9082ab70c8e30ff3985f918d60; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjM1MzgzNzE5OTIsImlzcyI6InVjIiwiZXhwIjoxNzM3NjQ1Nzc0LCJjdG0iOjE3MzUwNTM3NzQwNjYsImNpZCI6ImQ5ZDBuNEFadXAifQ.ZmgZ3tXhMxFp2ClHspHCp7gykoR4R3ke7j9RTUsCsQJwgkumigQn7iVlIgVxXlAesn3erl5io3G9EtQejb4udGDXwTKahOZ_i7qVtQVZu7XEQMLuGgylLyQiwymkvhWORFxuVs4Pioaf7Q_R2Tj-hQpzVxPcA3q5hRpXxdQRw1t4tdhL17i1FAHA9oK-uh3hB7U9bKPvwNC92l1hv-QMqwO_BcVFZ9g5LNqRsUh2ioDYeMSaBOKQd-w0ohoUbsbuuyFwPX4V28ifBVaQjHcmq9YEZKpcvv7gEVHU61jYTldsmkoARgjwDMeeVQdK_FAqRd79lyIQtbjcTWBqGF_ImA; xq_r_token=88dc57b31a81c93230c07d7ed7349d81599dd623; xq_is_login=1; u=3538371992; is_overseas=0; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1735053793; ssxmod_itna=QqAOYvxGhDO8GH=GdfOeeqBIxAKayDDt7QQi7ADlhcxxA5D8D6DQeGTiue+3b3=/nEwfNqiP4G=fepmir=ecn7Gfeflpe4GLDmKDyKereeDx1q0rD74irDDxD3DbSdDSDWKD9D0+kSBuqtDm4GWCqGfDDoDYR=nDitD4qDB+EdDKqGgCdEKW06PMS2MUjUxFlD9DDNyD0UQxBLxGZuow1FPSLdDtqDRDAtD8LyU4FjoS=XlIEx=U0+bjBGmC+iaiqGy0zylUuXXUC+B/TN4pBEKYD4s8GQnkrhm778YYixteoePWYpEtBD4CDriD=G+cOiQDDAlhN0GDD===; ssxmod_itna2=QqAOYvxGhDO8GH=GdfOeeqBIxAKayDDt7QQi7D6pfD0H307UDLxYI+D=',

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
