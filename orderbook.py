from random import random

from common import random_date
from config import client, API_ENDPOINT, FTX_API_KEY, FTX_SECRET_KEY
from typing import Optional, Dict, Any, List
from task import FtxClient


class OrderBook(FtxClient):
    def __init__(self, api_key=None, api_secret=None) -> None:
        super().__init__(api_key=api_key, api_secret=api_secret)

    def get_open_orders(self, market: str = None) -> List[dict]:
        return self._get(f'orders', {'market': market})

    def write_open_order_in_db(self, market: str = None) -> List[dict]:
        try:
            data = self.get_open_orders(market=market)
            result = [i.update({"measurement": "orders", "time": random_date()}) for i in data['result']]
            client.write_points(result)
        except:
            json_body = [{"measurement": "orders", "time": random_date(), "fields": {"market": market, "side": "buy",
                                                                                     'price': 12345.0, 'size': 1}}]
            client.write_points(json_body)


if __name__ == '__main__':
    obj = OrderBook(api_key=FTX_API_KEY, api_secret=FTX_SECRET_KEY)
    obj.write_open_order_in_db(market='BTC/USD')