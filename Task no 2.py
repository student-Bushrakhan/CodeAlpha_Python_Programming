  ##-----------  TASK NO. 2----------##
                ## ---------- Stock Portfolio Tracker ---------##
    

import yfinance as yf
import pandas as pd

# Initialize an empty portfolio
portfolio = {}

def add_stock(ticker, shares):
    if ticker in portfolio:
        portfolio[ticker] += shares
    else:
        portfolio[ticker] = shares
    print(f"Added {shares} shares of {ticker} to the portfolio.")

def remove_stock(ticker, shares):
    if ticker in portfolio:
        if shares >= portfolio[ticker]:
            del portfolio[ticker]
            print(f"Removed all shares of {ticker} from the portfolio.")
        else:
            portfolio[ticker] -= shares
            print(f"Removed {shares} shares of {ticker} from the portfolio.")
    else:
        print(f"{ticker} is not in the portfolio.")

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    return stock.history(period="1d")

def track_portfolio():
    total_value = 0
    portfolio_data = []

    for ticker, shares in portfolio.items():
        stock_data = get_stock_data(ticker)
        current_price = stock_data['Close'].iloc[-1]
        stock_value = current_price * shares
        total_value += stock_value
        portfolio_data.append({
            'Ticker': ticker,
            'Shares': shares,
            'Current Price': current_price,
            'Total Value': stock_value
        })

    portfolio_df = pd.DataFrame(portfolio_data)
    print("\nPortfolio Summary:")
    print(portfolio_df)
    print(f"\nTotal Portfolio Value: ${total_value:.2f}")

def main():
    while True:
        print("\nStock Portfolio Tracking Tool")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            ticker = input("Enter the stock ticker: ").upper()
            shares = int(input("Enter the number of shares: "))
            add_stock(ticker, shares)
        elif choice == '2':
            ticker = input("Enter the stock ticker: ").upper()
            shares = int(input("Enter the number of shares to remove: "))
            remove_stock(ticker, shares)
        elif choice == '3':
            track_portfolio()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()