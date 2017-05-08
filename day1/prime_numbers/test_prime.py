import unittest
from prime import gen_prime

class TestGenPrime(unittest.TestCase):
	def test_its_int (self):
		self.assertIs(type(gen_prime(3)[0]), int)

	def test_for_float (self):
		self.assertIs(type(gen_prime(3.5)[0]), int)


	def test_output_is_list (self):
		self.assertIs(type(gen_prime(3)), list)

	def test_output_is_odd_number (self):
		self.assertIs(gen_prime(3)[1]%2, 1)

	def test_when_input_is_one (self):
		self.assertEqual(gen_prime(1), 'prime numbers are positive and greater than one!')

	def test_when_input_is_zero (self):
		self.assertEqual(gen_prime(0), 'prime numbers are positive and greater than one!')

	def test_when_input_is_negative (self):
		self.assertEqual(gen_prime(-1), 'prime numbers are positive and greater than one!')

	def test_string_input (self):
		self.assertEqual(gen_prime('test'), 'Wrong entry')

	def test_list_input (self):
		self.assertEqual(gen_prime([]), 'Wrong entry')

	def test_dictionary_input (self):
		self.assertEqual(gen_prime({}), 'Wrong entry')

if __name__ == '__main__':
    unittest.main()