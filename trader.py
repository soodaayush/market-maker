import random

import numpy

# Trader types
trader_choices = ["random", "momentum", "informed"]
probability_trade = 0.6

class TraderClass:
    def __init__(self):
        pass

    def trade(self, prices, mid_price, new_mid_price):
        # Selects a trader type and makes a trade

        random_trader = random.choices(trader_choices, weights=(70, 20, 10))[0]

        if random_trader == "random":
            return self.random_trade()
        elif random_trader == "momentum":
            if len(prices) >= 5:
                return self.momentum_trade(prices)
            else:
                return self.random_trade()
        elif random_trader == "informed":
            return self.informed_trade(mid_price, new_mid_price)

    def random_trade(self):
        # Executes a random trade (buy or sell)

        action = random.choice(["BUY", "SELL", "NONE"])
        return action

    def momentum_trade(self, prices):
        # Executes a trade based on a price trend
        # If average of last 3 prices is larger than average of last 10 prices -> BUY
        # Else: -> SELL

        short_term_average_price = numpy.average(prices[-3:])
        long_term_average_price = numpy.average(prices[-10:])

        if random.random() < probability_trade:
            if short_term_average_price > long_term_average_price:
                return "BUY"
            else:
                return "SELL"
        else:
            return "NONE"

    def informed_trade(self, mid_price, new_mid_price):
        # Executes an informed trade based on future mid price

        if random.random() < probability_trade:
            if new_mid_price > mid_price:
                return "BUY"
        else:
            return "SELL"
