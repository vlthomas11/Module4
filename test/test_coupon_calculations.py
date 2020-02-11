import unittest
import unittest.mock as mock
from store import coupon_calculations as topic3


class TestCoupon(unittest.TestCase):
    def test_less_than_10(self):
        with mock.patch('builtins.input', side_effect=[10,5,10]):
            assert topic3.calculate_price(10,5,10) == 10.72

        with mock.patch('builtins.input', side_effect=[10, 5, 20]):
            assert topic3.calculate_price(10,5,20) == 10.19

        with mock.patch('builtins.input', side_effect=[10, 10, 20]):
            assert topic3.calculate_price(10,10,20) == 5.95

    def test_between_10_30(self):
        with mock.patch('builtins.input', side_effect=[25,5,10]):
            assert topic3.calculate_price(25,5,10) == 27.03
        with mock.patch('builtins.input', side_effect=[30,10,20]):
            assert topic3.calculate_price(30,10,20) == 24.91
        with mock.patch('builtins.input', side_effect=[23, 10, 15]):
            assert topic3.calculate_price(23, 10, 15) == 19.66

    def test_between_30_50(self):
        with mock.patch('builtins.input', side_effect=[35, 5, 10]):
            assert topic3.calculate_price(35, 5, 10) == 36.57
        with mock.patch('builtins.input', side_effect=[45, 10, 15]):
            assert topic3.calculate_price(45, 10, 15) == 39.48
        with mock.patch('builtins.input', side_effect=[49, 5, 20]):
            assert topic3.calculate_price(49, 5, 20) == 49.26

    def test_over_50(self):
        with mock.patch('builtins.input', side_effect=[60, 10, 10]):
            assert topic3.calculate_price(60, 10, 10) == 59.65

if __name__ == '__main__':
    unittest.main()
