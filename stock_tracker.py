import csv

def stock_portfolio_tracker():
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 330,
        "AMZN": 145
    }

    portfolio = []
    total_investment = 0

    print("=== Stock Portfolio Tracker ===")
    print("Available stocks & prices:")
    for symbol, price in stock_prices.items():
        print(f"  {symbol}: ${price}")
    print("\nEnter stock symbols and quantities (type 'done' to finish).\n")

    while True:
        symbol = input("Enter stock symbol (or 'done'): ").strip().upper()
        if symbol == "DONE":
            break

        if symbol not in stock_prices:
            print(f"'{symbol}' is not in the available stock list. Try again.\n")
            continue

        try:
            quantity = int(input(f"Enter quantity for {symbol}: "))
            if quantity <= 0:
                print("Quantity must be greater than 0.\n")
                continue
        except ValueError:
            print("Invalid quantity. Please enter a whole number.\n")
            continue

        price = stock_prices[symbol]
        investment = price * quantity
        total_investment += investment
        portfolio.append([symbol, quantity, price, investment])
        print(f"Added {quantity} shares of {symbol} (${investment}).\n")

    if not portfolio:
        print("No stocks added to the portfolio.")
        return

    print("\n=== Portfolio Summary ===")
    for item in portfolio:
        print(f"{item[0]} | Qty: {item[1]} | Price: ${item[2]} | Value: ${item[3]}")
    print(f"\nTotal Investment Value: ${total_investment}")

    save_choice = input("\nSave portfolio summary to 'portfolio_summary.csv'? (y/n): ").strip().lower()
    if save_choice == "y":
        with open("portfolio_summary.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Stock Symbol", "Quantity", "Price per Share ($)", "Total Value ($)"])
            writer.writerows(portfolio)
            writer.writerow(["TOTAL", "", "", total_investment])
        print("Saved successfully to 'portfolio_summary.csv'!")

if __name__ == "__main__":
    stock_portfolio_tracker()