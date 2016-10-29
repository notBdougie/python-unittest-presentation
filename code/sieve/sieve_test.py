#/usr/bin/env python3


import unittest
import sieve as s


class UtilTest(unittest.TestCase):
    """
    Class for the test function
    """

    def test_sieve_of_eratosthenes(self):
        """
        Test function that calls the real function and checks the return value
        """

        expected_return_value = [2, 3, 5, 7, 11]
        actual_return_value = list(s.sieve_of_eratosthenes(12))

        self.assertEqual(expected_return_value, actual_return_value)


if __name__ == '__main__':
        unittest.main()
