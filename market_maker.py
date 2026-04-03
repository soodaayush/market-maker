import random
import numpy

K = 3

def fill_order_book(spread, reservation_price):
    bid = round(reservation_price - (spread / 2), 2)
    ask = round(reservation_price + (spread / 2), 2)

    order_book = {"bid": {"bid": bid, "quantity": 1}, "ask": {"ask": ask, "quantity": 1}}

    return order_book

def adjust_mid_price(mid_price):
    random_num = round(random.uniform(-0.05, 0.05), 2)

    mid_price = round(mid_price + random_num, 2)

    return mid_price

def calculate_PnL(cash, inventory, prices, mid_price):
    total_pnl = cash + (inventory * mid_price)
    inventory_pnl = inventory * (mid_price - prices[len(prices) - 1])
    print((mid_price - prices[len(prices) - 1]))

    return total_pnl, inventory_pnl

def adjust_spread(spread, base_spread, prices):
    if len(prices) > 2:
        changes = numpy.diff(prices)
        volatility = numpy.std(changes)
        spread = base_spread + (K * volatility)
    else:
        spread = base_spread

    return spread