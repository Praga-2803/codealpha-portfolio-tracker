import time


STOCK_DATA = {
    'AAPL': 150.75,
    'GOOGL': 2750.45,
    'AMZN': 3401.46,
    'MSFT': 299.79,
    'TSLA': 730.91
}


portfolio = {}


def add_stock(ticker, quantity):
    if ticker in STOCK_DATA:
        if ticker in portfolio:
            portfolio[ticker] += quantity
        else:
            portfolio[ticker] = quantity
        print(f"{quantity} shares of {ticker} added to portfolio.")
    else:
        print(f"Error: {ticker} is not available in our stock list.")


def remove_stock(ticker, quantity):
    if ticker in portfolio:
        if portfolio[ticker] >= quantity:
            portfolio[ticker] -= quantity
            print(f"{quantity} shares of {ticker} removed from portfolio.")
            if portfolio[ticker] == 0:
                del portfolio[ticker]
        else:
            print(f"Error: Not enough shares of {ticker} to remove.")
    else:
        print(f"Error: {ticker} is not in your portfolio.")


def display_portfolio():
    if portfolio:
        print("\nYour Portfolio:")
        total_value = 0
        for ticker, quantity in portfolio.items():
            stock_value = STOCK_DATA[ticker] * quantity
            total_value += stock_value
            print(f"{ticker}: {quantity} shares, Value: ${stock_value:.2f}")
        print(f"Total Portfolio Value: ${total_value:.2f}\n")
    else:
        print("Your portfolio is empty.")


def main():
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add stock to portfolio")
        print("2. Remove stock from portfolio")
        print("3. View portfolio")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            ticker = input("Enter stock ticker symbol (e.g., AAPL, GOOGL): ").upper()
            try:
                quantity = int(input("Enter the quantity to add: "))
                add_stock(ticker, quantity)
            except ValueError:
                print("Invalid input. Quantity must be an integer.")
        
        elif choice == '2':
            ticker = input("Enter stock ticker symbol (e.g., AAPL, GOOGL): ").upper()
            try:
                quantity = int(input("Enter the quantity to remove: "))
                remove_stock(ticker, quantity)
            except ValueError:
                print("Invalid input. Quantity must be an integer.")
        
        elif choice == '3':
            display_portfolio()

        elif choice == '4':
            print("Exiting the tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

        
        time.sleep(1)


if _name_ == "_main_":
    main()