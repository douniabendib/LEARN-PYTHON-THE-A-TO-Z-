import unittest
import string_utils

class TestStringUtils(unittest.TestCase):
  def test_reverse_string(self):
    string = string_utils.reverse_string('Hello world') 
    self.assertEqual(string, 'dlrow olleH')


  def test_capitalize_string(self):
    string_capitalize = string_utils.capitalize_string('hello world')
    self.assertEqual(string_capitalize, 'Hello world')


  def test_is_capitalize(self):
    self.assertTrue(string_utils.is_capitalized('Hello'))
    self.assertFalse(string_utils.is_capitalized('hello'))


if __name__ == '__main__':
  unittest.main()
