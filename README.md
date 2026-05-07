# Market Maker

A Python implementation of a market maker, a trading system that continuously places buy and sell order to provide liquidity to the market and facilitates efficient asset trading. 

## Features

- Simulates bid and ask pricing with a dynamic mid-price  
- Updates mid-price using stochastic (random) movements  
- Adjusts reservation price based on inventory levels:  
	- Lowers prices when inventory is high to encourage selling  
	- Raises prices when inventory is low to encourage buying  
- Dynamically adjusts spread based on market volatility  
- Simulates multiple trader types for realistic market behavior:  
	- **Random Trader**: places random buy and sell orders  
	- **Momentum Trader**: buys during upward trends and sells during downward trends  
	- **Informed Trader**: trades based on knowledge of future price movements  
- Tracks performance metrics including:  
	- Total Profit and Loss (PnL)  
	- Inventory-based PnL  
- Provides data visualization using Matplotlib

## Inspiration

I have always been curious about finance, especially as I get closer to adulthood and will need to navigate things like credit cards, loans, and investments. While I had some basic knowledge of the stock market, I wanted to deepen my understanding.  
  
One question that stood out to me was how traders are able to buy and sell assets in real time with little to no interruption or error. This curiosity ultimately led me to explore how markets function behind the scenes, particularly the role of market makers.

## What is a Market Maker?

The description provided in the first line of the README would not have made much sense to me when I first started this project months ago, as it contained a lot of jargon I did not fully understand. When explaining a concept, I prefer using analogies rather than relying on highly abstract ideas.

### The Analogy

Imagine someone running a Pokémon card store. They always have cards to sell to you and are always willing to buy cards from you.

Now suppose they set fixed prices:

- If you want to sell your card, they buy it from you for $5  
- If you want to buy a card, they sell it to you for $6  

Notice that they buy at a lower price and sell at a higher price. This difference ensures the vendor makes a profit. In financial terms, this is called the *spread*.

### Translating to Financial Markets

In real markets, a market maker is typically a firm like Citadel Securities. Instead of trading Pokémon cards, they facilitate the buying and selling of financial assets such as stocks, bonds, ETFs, and cryptocurrencies.

They continuously quote two prices:

- **Bid price**: the price at which they are willing to buy  
- **Ask price**: the price at which they are willing to sell  

The difference between the bid and ask prices is the *spread*, which is how market makers generate profit.

## Installation

1. Clone the repository

```bash
git clone https://github.com/soodaayush/market-maker.git
cd market-maker
```

2. Install the required dependencies

```bash
pip install -r requirements.txt
```

 3. Run the project
 
 ```bash
python main.py
```
