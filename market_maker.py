import random
import numpy

K = 3

class MarketMaker:
    def __init__(self, spread, mid_price, cash, inventory, prices, base_spread, skew_factor):
        self.spread = spread
        self.mid_price = mid_price
        self.cash = cash
        self.inventory = inventory
        self.prices = prices
        self.base_spread = base_spread
        self.skew_factor = skew_factor

    def get_reservation_price(self, mid_price):
        return mid_price - self.inventory * self.skew_factor

    def fill_order_book(self, reservation_price):
        bid = round(reservation_price - (self.spread / 2), 2)
        ask = round(reservation_price + (self.spread / 2), 2)

        order_book = {"bid": {"bid": bid, "quantity": 1}, "ask": {"ask": ask, "quantity": 1}}

        return order_book

    def adjust_mid_price(self):
        random_num = round(random.uniform(-0.05, 0.05), 2)

        mid_price = round(self.mid_price + random_num, 2)

        return mid_price

    def calculate_pnl(self):
        total_pnl = self.cash + (self.inventory * self.mid_price)
        inventory_pnl = 0

        if len(self.prices) > 1:
            inventory_pnl = self.inventory * (self.mid_price - self.prices[-2])
        else:
            inventory_pnl = 0

        return total_pnl, inventory_pnl

    def adjust_spread(self, prices):
        if len(prices) > 2:
            changes = numpy.diff(self.prices)
            volatility = numpy.std(changes)
            return self.base_spread + (K * volatility)

        return self.base_spread

    def buy(self, price):
        self.inventory -= 1
        self.cash += price

    def sell(self, price):
        self.inventory += 1
        self.cash -= price