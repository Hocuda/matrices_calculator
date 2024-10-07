import unittest
from matrix import Matrix3x3

matrix_value = [1, 2, 3, 4, 5, 6, 7, 8, 9]

class TestMatrix3x3(unittest.TestCase):
	"""Тест для класса Matrix3x3"""

	def test_sum_m(self):
		matrix1 = matrix_value.copy()
		matrix2 = matrix_value.copy()
		test_main = Matrix3x3(matrix1, matrix2)
		result = test_main.sum_m()
		desired_result = '\n[2, 4, 6]\n[8, 10, 12]\n[14, 16, 18]'
		self.assertEqual(result, desired_result)

	def test_multiply_m_on_n(self):
		matrix1 = matrix_value.copy()
		number = 10
		test_main = Matrix3x3(matrix1)
		result = test_main.multiply_m_on_n(number)
		desired_result = '\n[10, 20, 30]\n[40, 50, 60]\n[70, 80, 90]'
		self.assertEqual(result, desired_result)


	def test_multiply_m_on_m(self):
		matrix1 = matrix_value.copy()
		matrix2 = matrix_value.copy()
		test_main = Matrix3x3(matrix1, matrix2)
		result = test_main.multiply_m_on_m()
		desired_result = '\n[30, 36, 42]\n[66, 81, 96]\n[102, 126, 150]'
		self.assertEqual(result, desired_result)

	def test_transpose_m(self):
		matrix1 = matrix_value.copy()
		test_main = Matrix3x3(matrix1)
		result = test_main.transpose_m()
		desired_result = '\n[1, 4, 7]\n[2, 5, 8]\n[3, 6, 9]'
		self.assertEqual(result, desired_result)

if __name__ == '__main__':
	unittest.main()