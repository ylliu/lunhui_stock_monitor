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

    'Cookie': 'cookiesu=321725805251564; device_id=69f1f5a469fccf1ee372b2db1abcbd29; smidV2=20240908222053d89f7239ebb1cbb6f1bf9e06ede5b4fc00603ec6af9a025d0; s=b216gletcb; bid=511229b42dcdeff49344a766a8e365a9_m0tnywjd; remember=1; xq_is_login=1; u=3538371992; .thumbcache_f24b8bbe5a5934237bbc0eda20c1b6e7=cXCYmZVwoJ1cZ4X271XDTAcRWu20ze3bv6yt5REQtnS5zfGV6LlBF8n9QMnXc/0dMlgXYHxxOJ/24loWyN9Ddw==; Hm_lvt_1db88642e346389874251b5a1eded6e3=1730547859,1731722180; acw_tc=2760825f17324613269325016ede8a1f6a4ed989277da3d07a8afe2de5c35c; xq_a_token=675561bbbbbe85a42eb847b33caeed575c0273fb; xqat=675561bbbbbe85a42eb847b33caeed575c0273fb; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjM1MzgzNzE5OTIsImlzcyI6InVjIiwiZXhwIjoxNzM1MDUzMzI2LCJjdG0iOjE3MzI0NjEzMjY5NTMsImNpZCI6ImQ5ZDBuNEFadXAifQ.T0FNLysuSNbHfu42LmKB5TfMxZ-YV7-dPP5QOnYvMCeVHpHDiPyV3RMWQiJvLAv2PshhOekINxAwy250-OUsOjhH76vOg7cWEc7X48FgKH6VlmCN_N1EBzaMdtCGGpxIcoWmnD41qusJXCtBa8x5xo49zX7kIm7J8Sw_caLXGRI2QuUlY7JGfb1wid-r6AtZIFNCSdpKLk12fkkMtKhnvC56XmfYdOaaV_p0gXMk0n020PQ1klI09hQQUZy1kgQriOzb1ad3uI2SkXsy-3TH4d63PpLXNncPRffmR7gd5zHDF8l4uWqh3Rey6GgIMX9aa4ERD9KMk-km60va5U9ozQ; xq_r_token=b323d2d4ff75db26f2677a2c0c0ad42a61820721; snbim_minify=true; ssxmod_itna=QqjhAKYIeRhTGQDXGDHD0Wvo0=qYD=ehiH15W5QboDlpG4A5D8D6DQeGTbcGDBChRPY5UCBiL+q71AidseDZ+ivFCA9+2GFxH4B3DEx06NbloxiigDCeDIDWeDiDG4GmeqGtDpxG=Djey1M2yCDYPDEe5DaxDbDiWCLxGCDeKD0=q7DQKDuPyYHevwGoEz8+yDtR0kDGHCD75vDlcDRKfpuFMPD4KDvxDODW5D6Zd7qVrPVR5scDx58mr4HmxqKDRh6jKDX61XlEHG+EOPno7s5bhWhYriiC9S0CxxHD+cbDRPzBTTWvGeCD4t0z/DeCGP6qhHDDi=6V6DoQDxD=; ssxmod_itna2=QqjhAKYIeRhTGQDXGDHD0Wvo0=qYD=ehiH15W5QD664GqxDsfQDLQYFTQl0eqnb4TcUCuP0KeXgdYxpqUDeev8VtCdxi4ofUBKYEtVOLDifxXP=72+GWs6YN61TwmtAjVeMfIkGiGALDpu3U4+diDuf+/hfR/ODq5AUs4E3iAnL3H4AordbGjxRQXS5Qh4oNX4aKrCG7lnKit+2oh05K5Qf8LgDcmjNYSjfoxZ5/8lKOCfAbt3EBzZwv+SGDN=3H0jwS70odx1L8b0ogbGX+u44/t=LqC+jABDTOw8GoNG3KKihiu67tAPq2=WEvbxh+ZK2mew2XUm0VCKnEIY1E/AIeapLD4hPmDPvwmjB0ehi6VWpD2ht8ARrd=9LjQ08GisexWzqhghvWTs=UR2uL7oVCGocG+iDKAGlmr5p521=Qtoi/5Q6owxxobot9P9crPGb5PiYaaY0pNlvFZTGGQRn2uWR4zIaPb=xyylbVWEbaRl4AfiplbF3hjnhmDpjxebxkQFF5KPX70YnZfR/0ke0eWa5p6fAFmcU7mgVF5RcOje8mpGog5ayPuFTq6gYsTw+evGElRvar2z=THldl2Eq=Tjj4DQFqWrAgbLqxH70u3+fq8+Lx5Cx9H/BCY4gwizPCVKFMqW3h9d0Q5Vcq6nNDI429Ui+PIHbGMvoTLOuKrSd45UGdAb85e0sDbrm1pe4r1CxenNzh4tTae5mDD08DG7rhiCd5h3oDD===',

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
