import unittest

from stock_monitor import StockMonitor


class TestStockMonitor(unittest.TestCase):
    def test_should_get_stock_of_user(self):
        stock_monitor = StockMonitor()
        stocks = stock_monitor.get_self_stocks()
        self.assertEqual(17, len(stocks))
        self.assertEqual(True, isinstance(stocks, list))

    def test_should_send_message_to_dingtalk_group(self):
        stock_monitor = StockMonitor()
        stock_monitor.send_message('赛里斯', '精研科技')
