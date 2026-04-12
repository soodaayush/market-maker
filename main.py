# Market Maker
import time

from market_maker import MarketMaker
from trader import TraderClass

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
MAX_TICKS = 20
TICKER = 0
MID_PRICE = 100
CASH = 500
INVENTORY = 0
MAX_INVENTORY = 20
MIN_INVENTORY = -20
SKEW_FACTOR = 0.01

prices = []
spread = 0

market_maker = MarketMaker(spread, MID_PRICE, CASH, INVENTORY, prices, BASE_SPREAD, SKEW_FACTOR)
trader = TraderClass()

while TICKER < MAX_TICKS:
    reservation_price = market_maker.get_reservation_price(MID_PRICE)
    TICKER += 1

    if len(prices) > 50:
        prices.pop(0)


    spread = market_maker.adjust_spread(prices)
    order_book = market_maker.fill_order_book(reservation_price)
    new_mid_price = market_maker.adjust_mid_price()

    action = trader.trade(prices, MID_PRICE, new_mid_price)

    if action == "BUY":
        price = order_book["ask"].get("ask")
        market_maker.sell(price)
    elif action == "SELL":
        price = order_book["bid"].get("bid")
        market_maker.buy(price)
    else:
        price = 0

    MID_PRICE = new_mid_price
    total_pnl, inventory_pnl = market_maker.calculate_pnl()

    prices.append(MID_PRICE)

    print(f"Tick: {TICKER}")
    print(f"Mid Price: ${market_maker.mid_price}")
    print(f"Market Maker Quote: Bid=${order_book['bid'].get('bid')} Ask=${order_book['ask'].get('ask')}")
    print(f"Trader Action: {action}")
    print(f"Trade Price: ${price}")
    print(f"Inventory: {market_maker.inventory}")
    print(f"Cash: ${round(market_maker.cash, 2)}")
    print(f"Total PnL: ${round(total_pnl, 2)}")
    print(f"Inventory PnL: ${round(inventory_pnl, 2)}")

    print("\n")

    time.sleep(5)