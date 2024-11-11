# Function to summarize the total value of buy and sell trades
def summarize_trades(trades):
    # Calculate the total value of buy trades
    buy_total = sum(trade.calculate_value() for trade in trades if trade.side == 'buy')
    # Calculate the total value of sell trades
    sell_total = sum(trade.calculate_value() for trade in trades if trade.side == 'sell')
    return buy_total, sell_total

# Function to filter trades and then summarize them
def filter_and_summarize(trades, filter_func):
    # Filter trades using the provided filter function
    filtered_trades = list(filter(filter_func, trades))
    # Summarize the filtered trades
    return summarize_trades(filtered_trades)

# Function to print summary statistics
def print_summary_statistics(trades):
    # Print the total value of all trades
    buy_total, sell_total = summarize_trades(trades)
    print(f"Total value of all trades:")
    print(f"  Total amount spent on purchases: ${buy_total:.2f}")
    print(f"  Total amount received from sales: ${sell_total:.2f}")

    # Prompt for and filter by a specific stock symbol
    symbol = input("Enter a specific stock symbol to filter by: ")
    buy_total, sell_total = filter_and_summarize(trades, lambda trade: trade.symbol == symbol)
    print(f"Total value of trades for symbol {symbol}:")
    print(f"  Total amount spent on purchases: ${buy_total:.2f}")
    print(f"  Total amount received from sales: ${sell_total:.2f}")

    # Prompt for and filter by a specific exchange
    exchange = input("Enter a specific exchange to filter by: ")
    buy_total, sell_total = filter_and_summarize(trades, lambda trade: trade.exchange == exchange)
    print(f"Total value of trades for exchange {exchange}:")
    print(f"  Total amount spent on purchases: ${buy_total:.2f}")
    print(f"  Total amount received from sales: ${sell_total:.2f}")

# Main program to print summary statistics
if __name__ == "__main__":
    # Prompt the user for the file path
    file_path = input("Enter the path to the trades.csv file: ")
    # Read the file and create trades
    trades = read_trading_log(file_path)
    # Print summary statistics
    print_summary_statistics(trades)
