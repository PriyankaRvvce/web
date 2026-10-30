
import unittest
from app import add


class TestAddition(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 20), 30)

    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)


if __name__ == "__main__":
    unittest.main()
