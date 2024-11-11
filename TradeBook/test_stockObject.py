# importing library for testing 
import unittest
from stock import Stock # type: ignore


class Test_Stocking(unittest.TestCase):
    def setUp(self):
        # Stock Object creation
        self.stock = Stock("ID541","CHX",230.000,2000, "SELL")

    # testing for to check the stock creation object
    def test_for_stock_object(self):
        self.assertEqual(self.stock.trade_id, "ID541")
        self.assertEqual(self.stock.exchange, "CHX")
        self.assertEqual(self.stock.price, 230.000)
        self.assertEqual(self.stock.quantity, 2000)
        self.assertEqual(self.stock.side,"SELL")

    # testing for value 
    def test_for_cal_value(self):
        self.assertEqual(self.stock.cal_value(), 230.000 * 2000)

if __name__ == "__main__":
    unittest.main()


