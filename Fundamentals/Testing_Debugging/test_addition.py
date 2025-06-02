import unittest


# Function to test: add two numbers
def add(a, b):
  return a + b


# Test case class for testing the add function
class AdditionNumbers(unittest.TestCase):
  # Define the first unit test
  def test_add(self):
    result = add(5, 2)


    # Define the expected result
    expected_result = 7
    self.assertEqual(result, expected_result)


if __name__ == '__main__':
  unittest.main()
