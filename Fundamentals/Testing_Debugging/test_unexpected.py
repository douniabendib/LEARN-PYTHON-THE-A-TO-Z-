import unittest
import unexpected


class TestUnexpected(unittest.TestCase):
  def test_get_sqrt(self):
    # Test valid square root
    self.assertEqual(unexpected.get_sqrt(144), 12)

    # Test for ValueError when input is negative
    with self.assertRaises(ValueError) as context:
      unexpected.get_sqrt(-1)
    self.assertIn("math domain error", str(context.exception))


  def test_divide(self):
    # Test valid division
    self.assertEqual(unexpected.divide(144, 12), 12)

    # Test for ZeroDivisionError
    with self.assertRaises(ZeroDivisionError) as context:
      unexpected.divide(10, 0)
    self.assertIn("division by zero", str(context.exception))


if __name__ == "__main__":
  unittest.main()
