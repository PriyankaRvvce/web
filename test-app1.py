
import unittest
from app1 import add


class TestAddition(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(20, 20), 30)

    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)


if __name__ == "__main__":
    unittest.main()
