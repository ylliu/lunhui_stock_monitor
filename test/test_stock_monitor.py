import unittest
from unittest import TestCase

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

    def test_get_add_stocks(self):
        stock_monitor = StockMonitor()
        stocks = ['赛里斯', '精研科技', '中国银河']
        previous_stocks = ['赛里斯', '精研科技']
        add_stocks = stock_monitor.get_add_stocks(stocks, previous_stocks)
        self.assertEqual(['中国银河'], add_stocks)

    def test_get_remove_stocks(self):
        stock_monitor = StockMonitor()
        stocks = ['赛里斯', '精研科技']
        previous_stocks = ['赛里斯', '精研科技', '中国银河']
        remove_stocks = stock_monitor.get_remove_stocks(stocks, previous_stocks)
        self.assertEqual(['中国银河'], remove_stocks)
