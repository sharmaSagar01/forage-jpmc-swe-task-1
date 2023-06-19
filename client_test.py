import unittest
from client3 import getDataPoint
from client3 import getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        print("-------------- Calculate the Stock Price -------------------------")
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            expected_reuslt = (quote['top_ask']['price'] +
                               quote['top_bid']['price'])/2
            stockName, top_price, ask_price, outputPrice = getDataPoint(quote)
            self.assertEqual(outputPrice, expected_reuslt)
            print('Calculating price Test passed')

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        print("---------------- Calculate the stock price where Bid price is greater than ask price --------------")
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """

        for quote in quotes:
            if quote['top_bid']['price'] > quote['top_ask']['price']:
                expected_result = (quote['top_ask']['price'] +
                                   quote['top_bid']['price'])/2
                stockName, bid_price, ask_price, outputPrice = getDataPoint(
                    quote)
                self.assertEqual(outputPrice, expected_result)
                print("Bid Greater than Ask Test is Passed")
            else:
                print('Bid is not greater than Ask')

    """ ------------ Add more unit tests ------------ """

    def test_getRatio_CalculateRatio(self):
        print("---------------- Calculate the Ration of Ask price and Bid price-----------")
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        for quote in quotes:
            ask_price = quote['top_ask']['price']
            bid_price = quote['top_bid']['price']
            if (bid_price == 0):
                print('Cannot create a ratio because the bid price is zero')
            else:
                expected = ask_price/bid_price
                output = getRatio(ask_price, bid_price)
                self.assertEqual(output, expected)
                print("Test Passed ....")


if __name__ == '__main__':
    unittest.main()
