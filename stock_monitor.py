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

    'Cookie': 'cookiesu=531697009482156; s=ci11otmhgx; device_id=61e2e2be4f4f13dabf4adc6cb76226ec; remember=1; xq_is_login=1; u=3538371992; xq_a_token=bc03d938f0ac9e28cef7156ca7826f35bed62732; xqat=bc03d938f0ac9e28cef7156ca7826f35bed62732; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjM1MzgzNzE5OTIsImlzcyI6InVjIiwiZXhwIjoxNzMwMTc4NjU1LCJjdG0iOjE3Mjc1ODY2NTUxNDcsImNpZCI6ImQ5ZDBuNEFadXAifQ.Rht3cjYx22jB-M_CXv1Axe7F2YfpY-76_-79YROhMNroM-kFQyWfDByyXE7x98-8GsZQBduodIOswOef1UINn1ebL-MNsqXZ7As4xFvIt7PyCgIY939118sx91cCKPMLOC4AykTHNdnCYZJZ3ZtQJnNFIlTPn5nxo01H4tqVKYTubk2uuzQ0iMddNn2_mRG2IluPBgne6akvMZJmUuuox7e9q6aI3hw2dBGpSIumQqSprDan0nVGHlQ42AnTA5_lrfOi0qnT3MrAL_Xs8asz3xtuSx-MoKqBhunacRCd27URWFXGccB7ZN-FATf_2GFJH9fI0SUZBE4u4Jm80T8U4g; xq_r_token=f3c44301f119d3db740d2d1006d33db2b568d3be; acw_tc=0bd17c6617275866559807482e53dbe84afc7e15454855934e1f05cccec83e; Hm_lvt_1db88642e346389874251b5a1eded6e3=1725442018,1727586654; HMACCOUNT=C8AD1976B369C03F; bid=511229b42dcdeff49344a766a8e365a9_m1n4x89r; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1727587408; ssxmod_itna=QqGOGKD5SYiKGHtGdmOeeqBKvKWT+FqyKm9DeKDs7ziDSxGKidDqxBenj4hnw5xNzWxePKDgBGDd4dWx0IKiZBicxQqWgAqmqiDCPGnDB9GYzxen=D5xGoDPxDeDADYE2DAqiOD7qDd21yzl=5Dbxi32xDbDiWCLxGCDeKD0PT7DQKDuPyTPe5whxEz7+yDQznkDGHCD7vIDlcD0biCWKMjeD77DCKDmxi1DnIXhojOTBdsl=T5H7xKe72rNPchfjKDXp=XlEHGwhgeno7s532x8gaNtmiH8c4xN2Dc1hxF1epnIB0r510rb0xni3GiNSxKDDWN21zxq4D==; ssxmod_itna2=QqGOGKD5SYiKGHtGdmOeeqBKvKWT+FqyKm9DikA7tzDl=DmuD03toD9iu/SCCiqidjAgxTQHqEhd9bOobI0x6en3epG=L7bfE3I8qBKeyW=kT3TBW2EN5jScG+PzUZiN4uN0rSSF5YoQe4wZY0pjK4ALI8A0tC0hR8DCCO0j0hLEImd1482qZQUqLOY9Gm0oNYoG/mI7fj2PH=XGQnpI4RUqkPY5mqYaPlbLtW21jfXG8+6HYqgx4WH6Ajd8BW0j0/goatXU6tY9WU32TKr46S5HD8iOCgQ0c2ZDo8Rq1ivkN7i1URwlev/AhjGhMhLxcmLGxqFmu2Xg6xk0xw=w+jdF2QQ3UxrmA235fh3hhfQEHCGB1tEiYig45mAqAq5lR3gAcj2YhxVP34gUqadV2pb=AqGmY1fABhuY+1nharQNj3IaQWDG2niQt+pR+NmgDRqFc3q6rQ62Hsas87hKnXRqDhW5=+OuwxwxDFqD+rDxD===',

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
