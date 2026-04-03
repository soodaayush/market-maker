# Market Maker
import random
import time

from market_maker import fill_order_book, adjust_mid_price, calculate_PnL, adjust_spread

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

BASE_SPREAD = 0.1
TICKER = 0
MID_PRICE = 100
CASH = 500
INVENTORY = 0
MAX_INVENTORY = 20
MIN_INVENTORY = -20
SKEW_FACTOR = 0.01


prices = []
spread = 0


def trade(order_book):
    global INVENTORY, CASH

    trader_action = ""
    price = 0
    random_num = random.randint(0, 1)

    if random_num == 0 and INVENTORY > MIN_INVENTORY:
        trader_action = "BUY"
        ask_data = order_book["ask"]
        price = ask_data.get("ask")
        INVENTORY -= 1
        CASH += price
    elif random_num == 1 and INVENTORY < MAX_INVENTORY:
        trader_action = "SELL"
        bid_data = order_book["bid"]
        price = bid_data.get("bid")
        INVENTORY += 1
        CASH -= price

    return trader_action, price


while True:
    reservation_price = MID_PRICE - (INVENTORY * SKEW_FACTOR)
    prices.append(MID_PRICE)
    TICKER += 1

    spread = adjust_spread(spread, BASE_SPREAD, prices)
    order_book = fill_order_book(spread, reservation_price)
    action, price = trade(order_book)
    total_pnl, inventory_pnl = calculate_PnL(CASH, INVENTORY, prices, MID_PRICE)
    MID_PRICE = adjust_mid_price(MID_PRICE)

    print(f"Tick: {TICKER}")
    print(f"Mid Price: {MID_PRICE}")
    print(f"Market Maker Quote: Bid=${order_book['bid'].get('bid')} Ask=${order_book['ask'].get('ask')}")
    print(f"Trader Action: {action}")
    print(f"Trade Price: ${price}")
    print(f"Inventory: {INVENTORY}")
    print(f"Cash: ${round(CASH, 2)}")
    print(f"Total PnL: ${round(total_pnl, 2)}")
    print(f"Inventory PnL: ${round(inventory_pnl, 2)}")

    print("\n")

    time.sleep(5)