# Market Maker

A Python implementation of a market maker, a trading system that continuously places buy and sell order to provide liquidity to the market and facilitates efficient asset trading. 

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
