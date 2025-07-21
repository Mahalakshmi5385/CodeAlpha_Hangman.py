stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 135
}

portfolio = {}
total_investment = 0

print("Stock Portfolio Tracker")
print("Available stocks: ", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not recognized. Try again.")
        continue
    quantity = input(f"How many shares of {stock} do you own? ")
    if not quantity.isdigit():
        print("Please enter a valid number.")
        continue
    quantity = int(quantity)
    portfolio[stock] = quantity
    total_investment += stock_prices[stock] * quantity

print("\nYour Portfolio Summary:")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares at ${stock_prices[stock]} each")

print(f"\nTotal Investment: ${total_investment}")