import unittest
from matrix import Matrix3x3

class TestMatrix3x3(unittest):
	"""Тест для класса Matrix3x3"""

	def test_multiply_m_on_m(self):
		matrix1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		matrix2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		matrix_test_var = Matrix3x3(matrix1, matrix2)
		result = matrix_test_var.multiply_matrix_on_matrix()
		desired_result = [30, 36, 42, 66, 81, 96, 102, 126, 150]
		self.assertEqual(result, desired_result)

if __name__ == 'main':
	unittest.main()