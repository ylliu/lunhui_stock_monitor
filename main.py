import time
from datetime import datetime

from stock_monitor import StockMonitor

if __name__ == "__main__":
    stock_monitor = StockMonitor()
    stocks = []
    send_times = [8, 12, 15, 20]
    while True:
        time.sleep(1)
        previous = stocks
        stocks = stock_monitor.get_self_stocks()
        if isinstance(stocks, str):
            stock_monitor.send_message2("系统异常，请检查cookie是否过期", stocks)
            time.sleep(60)
        add_stocks = stock_monitor.get_add_stocks(stocks, previous)
        remove_stocks = stock_monitor.get_remove_stocks(stocks, previous)
        stock_monitor.send_message(add_stocks, remove_stocks)
        stock_monitor.send_message_to_wechat(add_stocks, remove_stocks)
        current_time = datetime.now()
        current_hour = current_time.hour
        current_minute = current_time.minute
        if current_hour in send_times and current_minute == 0:  # 确保是整点
            stock_monitor.send_message2("轮回666小助手在线中", "")
