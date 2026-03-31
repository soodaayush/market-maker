# Market Maker
import random
import time

# - Program is based on a ticker, where
# 	- Mid prices are updated every tick to determine bid and ask using a specified spread (+- 0.5)
# 	- Every tick, market maker posts new bid and ask
# 	- Random trader decides to buy and sell
# 	- Inventory is updated
# 	- Record metrics of who bought what
# - Initializing simulator
# 	- Have one bid/ask price for first iteration
# 	- Set starting mid price
# 	- Set spread
# 	- Set starting inventory (shares held)
# 	- Set starting cash
# 	- Set number of ticks
# - Simulator Loop
# 	- Update mid price per tick
# 	- Market maker posts new quotes
# 		- $Bid = mid - spread/2$
# 		- $Ask = mid + spread/2$
# 	- Generate trader actions
# 		- Randomly choose to buy or sell
# 	- Execute trades:
# 		- Buy - > trader hits ask -> inventory - quantity, cash + price * quantity
# 		- Sell -> trader hits bid -> inventory + quantity, cash - price * quantity
# 	- Removed filled orders
# 	- Record metrics:
# 		- Inventory
# 		- Cash
# 		- PnL (Profit and Loss) = cash + inventory * mid price
# 	- Next tick

# Global Variables

SPREAD = 0.1
TICKER = 0
MID_PRICE = 100
CASH = 500
INVENTORY = 100

def increment_ticker():
    global TICKER

    TICKER += 1

def fill_order_book():
    bid = round(MID_PRICE - (SPREAD / 2), 2)
    ask = round(MID_PRICE + (SPREAD / 2), 2)

    order_book = {}

    order_book["bid"] = {"bid": bid, "quantity": 1}
    order_book["ask"] = {"ask": ask, "quantity": 1}

    return order_book

def adjust_mid_price():
    global MID_PRICE
    random_num = round(random.uniform(-0.05, 0.05), 2)

    MID_PRICE = round(MID_PRICE + random_num, 2)

def trade(order_book):
    global INVENTORY, CASH

    trader_action = ""
    price = 0
    random_num = random.randint(0, 1)

    if random_num == 0:
        trader_action = "BUY"
        ask_data = order_book["ask"]
        price = ask_data.get("ask")
        INVENTORY -= 1
        CASH += price
    elif random_num == 1:
        trader_action = "SELL"
        bid_data = order_book["bid"]
        price = bid_data.get("bid")
        INVENTORY += 1
        CASH -= price

    return trader_action, price

def calculate_PnL():
    PnL = CASH + (INVENTORY * MID_PRICE)
    return PnL

while True:
    increment_ticker()
    order_book = fill_order_book()
    action, price = trade(order_book)
    PnL = calculate_PnL()
    adjust_mid_price()

    print(f"Tick: {TICKER}")
    print(f"Mid Price: {MID_PRICE}")
    print(f"Market Maker Quote: Bid=${order_book['bid'].get('bid')} Ask=${order_book['ask'].get('ask')}")
    print(f"Trader Action: {action}")
    print(f"Trade Price: ${price}")
    print(f"Inventory: {INVENTORY}")
    print(f"Cash: ${round(CASH, 2)}")
    print(f"PnL: ${round(PnL, 2)}")

    print("\n")

    time.sleep(5)