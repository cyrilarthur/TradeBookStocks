# Define a Tradebook class to categorize and analyze trades
class Tradebook:
    def __init__(self):
        self.reference_trades = []  # List to store reference trades
        self.small_trades = []  # List to store smaller trades
        self.large_trades = []  # List to store larger trades

    def add(self, trade):
        # Add a trade to the appropriate list
        if not self.reference_trades:
            # First trade is the reference trade
            self.reference_trades.append(trade)
        else:
            # Compare the current trade value with the first trade value
            first_trade_value = self.reference_trades[0].calculate_value()
            current_trade_value = trade.calculate_value()
            if current_trade_value > first_trade_value:
                self.large_trades.append(trade)
            elif current_trade_value < first_trade_value:
                self.small_trades.append(trade)
            else:
                self.reference_trades.append(trade)

    def print_statistics(self, trade_list, description):
        # Print the count and average value of trades in a list
        count = len(trade_list)
        average_value = sum(trade.calculate_value() for trade in trade_list) / count if count else 0
        print(f"{description} - Count: {count}, Average Value: ${average_value:.2f}")

    def print_reference_trades_statistics(self):
        self.print_statistics(self.reference_trades, "Reference Trades")

    def print_small_trades_statistics(self):
        self.print_statistics(self.small_trades, "Small Trades")

    def print_large_trades_statistics(self):
        self.print_statistics(self.large_trades, "Large Trades")

# Main program to monitor trader performance
if __name__ == "__main__":
    # Prompt the user for the file path
    file_path = input("Enter the path to the trades.csv file: ")
    # Read the file and create trades
    trades = read_trading_log(file_path)

    # Create a Tradebook instance
    tradebook = Tradebook()
    # Add each trade to the tradebook
    for trade in trades:
        tradebook.add(trade)

    # Print statistics for each category
    tradebook.print_reference_trades_statistics()
    tradebook.print_small_trades_statistics()
    tradebook.print_large_trades_statistics()
