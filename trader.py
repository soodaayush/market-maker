import random

from market_maker import MarketMaker

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


def trade(order_book, inventory, min_inventory, max_inventory, cash, prices, mid_price, new_mid_price):
    random_trader = random.choices(trader_choices, weights=(70, 20, 10))[0]
    trader_action = ""
    price = 0

    if random_trader == "random":
        trader_action, price, inventory, cash = random_trade(order_book, inventory, min_inventory, max_inventory, cash)
    elif random_trader == "momentum":
        if len(prices) >= 5:
            trader_action, price, inventory, cash = momentum_trade(order_book, inventory, cash, prices, mid_price)
        else:
            trader_action, price, inventory, cash = random_trade(order_book, inventory, min_inventory, max_inventory, cash)
    elif random_trader == "informed":
        trader_action, price, inventory, cash = informed_trade(order_book, inventory, cash, prices, mid_price, new_mid_price)

    return trader_action, price, inventory, cash

def random_trade(order_book, inventory, min_inventory, max_inventory, cash):
    trader_action = ""
    price = 0
    random_num = random.randint(0, 1)

    if random_num == 0 and inventory > min_inventory:
        trader_action = "BUY"
        price, inventory, cash = execute_trade(trader_action, order_book, inventory, cash)
    elif random_num == 1 and inventory < max_inventory:
        trader_action = "SELL"
        price, inventory, cash = execute_trade(trader_action, order_book, inventory, cash)

    return trader_action, price, inventory, cash

def momentum_trade(order_book, inventory, cash, prices, mid_price):
    recent_change = prices[-1] - prices[-5]
    trader_action = ""
    price = 0

    if recent_change > 0:
        trader_action = "BUY"
        price, inventory, cash = execute_trade(trader_action, order_book, inventory, cash)
    elif recent_change < 0:
        trader_action = "SELL"
        price, inventory, cash = execute_trade(trader_action, order_book, inventory, cash)
    else:
        trader_action = "NONE"

    return trader_action, price, inventory, cash

def informed_trade(order_book, inventory, cash, prices, mid_price, new_mid_price):
    trader_action = ""
    price = 0

    if new_mid_price > mid_price:
        trader_action = "BUY"
        price, inventory, cash = execute_trade(trader_action, order_book, inventory, cash)
    else:
        trader_action = "SELL"
        price, inventory, cash = execute_trade(trader_action, order_book, inventory, cash)

    return trader_action, price, inventory, cash

def execute_trade(decision, order_book, inventory, cash):
    price = 0

    if decision == "BUY":
        ask_data = order_book["ask"]
        price = ask_data.get("ask")
        inventory -= 1
        cash += price
    elif decision == "SELL":
        bid_data = order_book["bid"]
        price = bid_data.get("bid")
        inventory += 1
        cash -= price

    return price, inventory, cash