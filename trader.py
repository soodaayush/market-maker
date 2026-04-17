import random

trader_choices = ["random", "momentum", "informed"]

class TraderClass:
    def __init__(self):
        pass

    def trade(self, prices, mid_price, new_mid_price):
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
        action = random.choice(["BUY", "SELL", "NONE"])
        return action

    def momentum_trade(self, prices):
        recent_change = prices[-1] - prices[-5]

        if recent_change > 0:
            return "BUY"
        elif recent_change < 0:
            return "SELL"
        else:
            return "NONE"

    def informed_trade(self, mid_price, new_mid_price):
        if new_mid_price > mid_price:
            return "BUY"
        else:
            return "SELL"
