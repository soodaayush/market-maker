# Order Book
import random


class OrderBook():
    def __init__(self):
        self.order_book = {"bid": [], "ask": []}

    def generate_quote(self, reservation_price, base_spread):
        random_num = random.randint(0, 1)

        bid = round(reservation_price - (base_spread / 2), 2)
        ask = round(reservation_price + (base_spread / 2), 2)

        if random_num == 0:
            self.order_book["bid"].append({"price": bid, "quantity": 1})
        else:
            self.order_book["ask"].append({"price": ask, "quantity": 1})