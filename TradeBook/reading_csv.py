# Function to read the trading log from a CSV file and create Stock objects
def read_trading_log(file_path):
    trades = []  # List to store trades
    trade_id = 1  # Starting trade ID
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')  # Read the file using a CSV reader
        for row in reader:
            # Extract values from the row
            time, exchange, symbol, quantity, price, side = row
            # Generate a unique trade ID
            trade_id_str = f"id{trade_id}"
            # Create a Stock object
            stock = Stock(trade_id_str, exchange, symbol, float(price), int(quantity), side)
            # Add the stock to the list
            trades.append(stock)
            # Increment the trade ID
            trade_id += 1
    return trades


# Main program to read and process the trading log file
if __name__ == "__main__":
    # Prompt the user for the file path
    file_path = input("Enter the path to the trades.csv file: ")
    # Read the file and create trades
    trades = read_trading_log(file_path)

    # Print each trade to verify
    for trade in trades:
        print(trade)

        