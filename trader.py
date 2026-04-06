import random
import numpy

trader_choices = ["random", "momentum", "informed"]

def trade(order_book, inventory, min_inventory, max_inventory, cash, prices, mid_price):
    random_trader = random.choices(trader_choices, weights=(70, 20, 10))[0]
    trader_action = ""
    price = ""

    if random_trader == "random":
        trader_action, price = random_trade(order_book, inventory, min_inventory, max_inventory, cash)
    elif random_trader == "momentum" and len(prices) >= 5:
        trader_action, price = momentum_trade(order_book, inventory, cash, prices, mid_price)

    return trader_action, price

def random_trade(order_book, inventory, min_inventory, max_inventory, cash):
    trader_action = ""
    price = 0
    random_num = random.randint(0, 1)

    if random_num == 0 and inventory > min_inventory:
        trader_action = "BUY"
        ask_data = order_book["ask"]
        price = ask_data.get("ask")
        inventory -= 1
        cash += price
    elif random_num == 1 and inventory < max_inventory:
        trader_action = "SELL"
        bid_data = order_book["bid"]
        price = bid_data.get("bid")
        inventory += 1
        cash -= price

    return trader_action, price

def momentum_trade(order_book, inventory, cash, prices, mid_price):
    recent_change = mid_price - prices[-5]
    trader_action = ""
    price = 0

    if recent_change > 0:
        trader_action = "BUY"
        ask_data = order_book["ask"]
        price = ask_data.get("ask")
        inventory -= 1
        cash += price
    elif recent_change < 0:
        trader_action = "SELL"
        bid_data = order_book["bid"]
        price = bid_data.get("bid")
        inventory += 1
        cash -= price

    return trader_action, price

def informed_trade():
    pass