import unittest
from input_validation import validation_with_try as topic4


def test_average_exception(self):
    with self.assertRaises(ValueError):
        topic4.average(-90, 89, 78)


if __name__ == '__main__':
    unittest.main()
