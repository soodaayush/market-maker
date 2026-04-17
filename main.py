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

MAX_TICKS = 20
TICKER = 0

market_maker = MarketMaker()
trader = TraderClass()

while TICKER < MAX_TICKS:
    market_maker.update_reservation_price()
    TICKER += 1

    if len(market_maker.prices) > 50:
        market_maker.prices.pop(0)

    market_maker.adjust_spread()
    order_book = market_maker.fill_order_book()
    market_maker.adjust_mid_price()

    action = trader.trade(market_maker.prices, market_maker.mid_price, market_maker.new_mid_price)

    if action == "BUY":
        price = market_maker.order_book["ask"].get("ask")
        market_maker.sell(price)
    elif action == "SELL":
        price = market_maker.order_book["bid"].get("bid")
        market_maker.buy(price)
    else:
        price = 0

    market_maker.calculate_pnl()
    market_maker.prices.append(market_maker.mid_price)

    print(f"Tick: {TICKER}")
    print(f"Mid Price: ${market_maker.mid_price}")
    print(f"Market Maker Quote: Bid=${market_maker.order_book['bid'].get('bid')} Ask=${market_maker.order_book['ask'].get('ask')}")
    print(f"Trader Action: {action}")
    print(f"Trade Price: ${price}")
    print(f"Inventory: {market_maker.inventory}")
    print(f"Cash: ${round(market_maker.cash, 2)}")
    print(f"Total PnL: ${round(market_maker.total_pnl, 2)}")
    print(f"Inventory PnL: ${round(market_maker.inventory_pnl, 2)}")

    print("\n")

    time.sleep(5)