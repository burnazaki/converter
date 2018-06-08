import unittest
import converter


class TestConverter(unittest.TestCase):

    def test_result_value(self):
        self.assertTrue(converter.convert_currency(price_in_usd=1, to_currency="UAH") > 0)
        self.assertTrue(converter.convert_currency(price_in_usd=1, to_currency="GBP") > 0)
        self.assertTrue(converter.convert_currency(price_in_usd=1, to_currency="EUR") > 0)

    def test_invalid_input(self):
        self.assertRaises(ValueError, converter.convert_currency, price_in_usd=1, to_currency="BTC")
        self.assertRaises(ValueError, converter.convert_currency, price_in_usd=-1, to_currency="UAH")


if __name__ == '__main__':
    unittest.main()
