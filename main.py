# Market Maker

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

def ticker():
    pass

def fill_order_book():
    pass

def trade():
    pass

def setup():
    pass

def record_metrics():
    pass