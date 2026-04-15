import random
import numpy

K = 3

class MarketMaker:
    def __init__(self):
        self.mid_price = 100
        self.new_mid_price = 0
        self.cash = 500
        self.inventory = 0
        self.prices = []
        self.base_spread = 0.1
        self.skew_factor = 0.01
        self.inventory_pnl = 0
        self.total_pnl = 0
        self.order_book = {}
        self.reservation_price = 0

    def get_reservation_price(self):
        self.reservation_price = self.mid_price - self.inventory * self.skew_factor

    def fill_order_book(self):
        bid = round(self.reservation_price - (self.base_spread / 2), 2)
        ask = round(self.reservation_price + (self.base_spread / 2), 2)

        self.order_book = {"bid": {"bid": bid, "quantity": 1}, "ask": {"ask": ask, "quantity": 1}}

    def adjust_mid_price(self):
        random_num = round(random.uniform(-0.05, 0.05), 2)

        self.new_mid_price = round(self.mid_price + random_num, 2)

    def change_mid_price(self):
        self.mid_price = self.new_mid_price

    def calculate_pnl(self):
        self.total_pnl = self.cash + (self.inventory * self.mid_price)

        if len(self.prices) > 1:
            self.inventory_pnl = self.inventory * (self.mid_price - self.prices[-2])
        else:
            self.inventory_pnl = 0

    def adjust_spread(self):
        if len(self.prices) > 2:
            changes = numpy.diff(self.prices)
            volatility = numpy.std(changes)
            self.base_spread = self.base_spread + (K * volatility)
        else:
            self.base_spread = 0.01

    def buy(self, price):
        self.inventory -= 1
        self.cash += price

    def sell(self, price):
        self.inventory += 1
        self.cash -= price