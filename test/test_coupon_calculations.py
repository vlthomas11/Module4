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
            assert topic3.calculate_price(10,5,20) == 0

if __name__ == '__main__':
    unittest.main()
