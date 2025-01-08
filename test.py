import unittest
from source import  is_prime

from source import is_prime

class Prime(unittest.TestCase):
    def test_should_return_true_with_prime_number(self):
        self.assertEqual(is_prime(5), True)

    def test_should_return_false_with_prime_number(self):
        self.assertEqual(is_prime(4), False)

    def test_should_return_false_with_non_is_prime_one(self):
        self.assertFalse(is_prime(1))



if __name__ == "__main__":
    unittest.main()

