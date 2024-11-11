from abc import ABC, abstractmethod


class Trade(ABC):
    def __init__(self,trade_id, exchange, symbol, price, quantity, side):
        self.trade_id = trade_id
        self.exchange = exchange
        self.symbol = symbol
        self.price = price
        self.quantity = quantity
        self.side = side


    # abstract method 
    @abstractmethod
    def cal_value(self):
        pass
    
    # string representation of the trade object 
    def __str__(self):
        return (f"TradeID: {self.trade_id}, Exchange: {self.exchange}, 
                Symbol: {self.symbol}, Price: {self.price}, Qty: {self.quantity}, Side: {self.side}")
    

class Stock(Trade):
    # abstract method implementation 
    def cal_value(self):
        return self.price * self.quantity
    
    # overriding string representation of trade object
    def __str__(self):
        return (super().__str__() + f",Value: {self.cal_value()}")
    
        