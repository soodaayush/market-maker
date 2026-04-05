import random

trader_choices = ["random", "momentum", "informed"]

def trade(order_book, inventory, min_inventory, max_inventory, cash):
    print(random.choices(trader_choices, weights=(70, 20, 10)))

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

def random_trade():
    pass

def momentum_trade():
    pass

def informed_trade():
    pass