import json
import time
import requests

# 因为不能访问, 所以我们加个头试试
# headers = {
#     'Accept': 'application/json, text/plain, */*',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'cache-control': 'no-cache',
#     'Connection': 'keep-alive',
#
#     'Cookie': 'cookiesu=321725805251564; device_id=69f1f5a469fccf1ee372b2db1abcbd29; s=b216gletcb; bid=511229b42dcdeff49344a766a8e365a9_m0tnywjd; Hm_lvt_1db88642e346389874251b5a1eded6e3=1740296515; HMACCOUNT=743A1CF7652093E3; xq_a_token=fb47d58a8bc6c3fe95ea8e526e87424fb25f2f1e; xqat=fb47d58a8bc6c3fe95ea8e526e87424fb25f2f1e; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjM1MzgzNzE5OTIsImlzcyI6InVjIiwiZXhwIjoxNzQyODg4NjA0LCJjdG0iOjE3NDAyOTY2MDQyMjksImNpZCI6ImQ5ZDBuNEFadXAifQ.O7vpprTRSRBYPXzLCLJ5S_MMfztcjeV-eRmWrq9Ebxbr4eEHlJi9i35UHlkwzE9yl6zLmEwIKdyZG4q-dbwcpHehUccNYfaM51hq7ZODxyxdjC_C_d_uGVjpplu4WfPkStFOKahySo3j3Nd-prcDjLPHLtwXgWR3V737CvmRrzVzP9smP3sGIWhlMXwVXtzxHWpAxlXsYOutwQpj4yuiT2MpoX56h3Cd7bGlW9GW-Jw68mhsNG27_lZ-TVPN8P0PpWWqhjG-TujttdUDf3WgOvbWo_W3hbG3sgAvGcZ1AE-32XVboBGTDuG0DCKKGjxLNRKphfqCEL3q6n5hbDELzA; xq_r_token=e0e216430476e30e307f8c4bf7a6bbd3523cdcb3; xq_is_login=1; u=3538371992; acw_tc=0bd17c0617402966400502350eace7ee23fa31c92d040cbcdc93c62f3e792c; snbim_minify=true; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1740296873; ssxmod_itna=YqjxBDuDyDgGq+xl8DCxDT1Yx2ADnC=0CA0ZxWq8yGr5DsCLDSxGKidDqxBmnZvhdWehS+fHPrnxP44XQiBqbeCzEDRd5X/lrR3DHxY=DUZi+dDx6q0rD74irDDxD3Db8QDSDWKD9D0bCy65suxGWDmbCDWPDYxDr26KDRxi7DDH=hx07DQHCeQ0P2g77bfvIBhGwQlKDBP5D92oDsh0j+8o69zxGhx0ODiKDcxikD5K2NWx0l2y=qAGKO02POibW5/R8Dl99/RvzxtIIaivGZ1YPb=iH4c+eLduPeC25mDVP3GGxQa=5bCPK0DMOGNAGtYxhYetDDAA9VAKDPD=; ssxmod_itna2=YqjxBDuDyDgGq+xl8DCxDT1Yx2ADnC=0CA0ZxWq8yGxikUCAzDlg7Dj4vx3txSPKHArDyDwDViq2PCQ0hDx=D6mSwteHg0DpREQBBq33fI0aP3xfDNuEo4RTrWlk8fNtHCtcxHpqaxfBBYnR+fC3Qte1q3XWYNAK83euxtfz83ZWlj3aduuznREYj5dZ0YA++q8K7dC8Di8trd17YPN5GiejkWW5ixRz4p56cdtYB2EKQaxuZj/BPP4H90ry60Dv3gz/7cNVWnpa/A0Eww1O+XIKXrxT/ezNX6y+w2V9MM0jlZ11wwakcuA5L4w9G+xmcUzqqmPy0257BTURqmckKqrGbMnqWD7Kqx=8bNihW3eu/uklRnzcfFH7W0i3AdHccn5O4TYrYzImrCTtPv44pbbrp9PqWD4kbT7isUwqV0DUubZrTWGvFGttR5m4lfno7cTzETGSH4uVUBmShRi5UU9T4yr8bUmex8MxHuSKD3gTQv7Z+ogYoptdIfWCnamBuOivbFyan3Ys9qOAR8uqhflSxqDqQhKxKAOKiERgwmHWbA7QPSQR5xhrK7Wnh/mnczft4hvirtKBWS4tSesR2eZel+MxUdAtM2BeXYmIA2wK7NCIpiOl+61taX9RPCxDKM5QgR3Pxg75ZDl+iFhgKSG5lWl9/rZ22oBRpZqRVqHoHQmrvYV8raxTy5DRTZy4hePrU0eYmOPxoAr0W/5kn5PhQAsZHOrhsG493D08DG7qxxiDKcfj1dxen3=eDOD32G7D4D==',
#
#     'origin': 'https://xueqiu.com',
#     'Referer': 'https://xueqiu.com/u/8282709675',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 SE 2.X MetaSr 1.0',
#     'X-Requested-With': 'XMLHttpRequest'
# }

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'Connection': 'keep-alive',

    'Cookie': 'cookiesu=321725805251564; device_id=69f1f5a469fccf1ee372b2db1abcbd29; s=b216gletcb; bid=511229b42dcdeff49344a766a8e365a9_m0tnywjd; Hm_lvt_1db88642e346389874251b5a1eded6e3=1752761569; HMACCOUNT=743A1CF7652093E3; remember=1; xq_a_token=958407a432f029674433ba06b664876392dcbf57; xqat=958407a432f029674433ba06b664876392dcbf57; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjM1MzgzNzE5OTIsImlzcyI6InVjIiwiZXhwIjoxNzU1MzUzNjA3LCJjdG0iOjE3NTI3NjE2MDc1NDYsImNpZCI6ImQ5ZDBuNEFadXAifQ.geU6hSjm1lY59NdpPBcaoWw9dDyb6cds2UfsUx08tv6JRJE3dDTli3MQYaqPW8ULBbvkuRlfbv5QbtaYriraEoAv0KVhX2EP_ZdLAY_5PrMrppDGZ3dwne3TINKPVRDhM61FcpbNWcjpI68nKcZTgxDBZnIJDA-PJ0TN2oAKrc8qTEmZziPNcMl5wyvGWXf_RLtW-HcV5MItFVWf0uraKhUOCbN0HFvfOxHqZo1Kn_JrXrwAa9tXHWnWVlRRy95D58FFkUByIvKok9V7MHs2AUQ8BhosHOxMWTYKGGqQ2Gr1WfHDQMSu9F2SZEuYdAqI6q9T3Np4U3laNiTL-FoPSw; xq_r_token=7adf85924678baea65dd83cd0c6fd190f3fb82f3; xq_is_login=1; u=3538371992; is_overseas=0; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1752761623; ssxmod_itna=1-eqROAK4jOx8DODhatGOKG2iDCDp=Dl4BUtD2DIqGQGcD8gx0p37_FjW0xGktznaKDlGU3DGxWqPgD054iDnqD86DQeDvDcf2IwxcalD_x=ZOYvPPdyAArTP3zjWySIPojjr2IF9AF2hI87xg3bvCDxGLDY=DCL_5DOqiDYYLDBYD74G_DDeDixGm7eDSSDD9DGPtP6WTZeDEDYPtxA3Di4D_BnbDmd4DGd3P2BethLYt2arzMDwrLDyxKGTDjMeD/SGLr/HjcUYa2P8Ew1odxB6uxBQTM7aK2DINOZn7xgh905mwziR3F4skBxNA4hhDi8DkAxqA4H7GaBz4f4liG4li5xwGDDix4qp2Pfen6U9ZUBPEjQKZARpCm0WA_WAx0XC0qsDeBQ2sD_eBD1lGzjXMrDxD; ssxmod_itna2=1-eqROAK4jOx8DODhatGOKG2iDCDp=Dl4BUtD2DIqGQGcD8gx0p37_FjW0xGktznaKDlGU3DGxWqPGDDPRK=DEiyqDLWg0KfNkDGX_Wk=G803Cu9_0B_eB9Dj741qVeC9EpkcARk2NWWtAX8E_5R4LK9DmwDr2KNShCB25GWBh3ng55cjYxD',

    'origin': 'https://xueqiu.com',
    'Referer': 'https://xueqiu.com/u/3639429204',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 SE 2.X MetaSr 1.0',
    'X-Requested-With': 'XMLHttpRequest'
}


# urllib 的相关操作如下
url = 'https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json?pid=-1&category=1&size=1000&uid=3639429204'


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
