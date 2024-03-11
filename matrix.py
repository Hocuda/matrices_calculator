class Matrix3x3:
	"""
	Класс для математический действий с матрицами 
	"""
	def __init__(self, matrix1='', matrix2=''):
		"""Функция инициализации класса"""
		if matrix2:
			self.matrix1 = matrix1
			self.matrix2 = matrix2
		else:
			self.matrix1 = matrix1
	

	def sum_matrices(self):
		"""
		Принимает 2 ретурна от matrix_logic и записывает их в списки с номером 
		матрицы, потом через цикл вырезает из каждого списка 2 элемент, 
		потому-что первый это название матрицы и после сумма этих елементов 
		записывается в конец нового списка с результатами. После этого список с 
		результатами нарезаеться на 3 списка для красивого вывода.  
		"""
		del self.matrix1[0]
		del self.matrix2[0]
		matrix1_1 = self.matrix1
		matrix2_2 = self.matrix2
		matrix_result_sum = []
		for matrix_result in range(9):
			matrix1_for = matrix1_1.pop(0)
			matrix2_for = matrix2_2.pop(0)
			matrix_result = matrix1_for + matrix2_for
			matrix_result_sum.append(matrix_result)

		slice1 = matrix_result_sum[:3]
		slice2 = matrix_result_sum[3:6]
		slice3 = matrix_result_sum[6:]
		pretty_matrix_result_sum = f"\n{slice1}\n{slice2}\n{slice3}"

		print ("\nResult of sum:", pretty_matrix_result_sum)


	def multiply_matrix_on_numbers(self, number):
		"""
		Умножает матрици на числа. Каждый элемент матрици умножается на 
		введенное число и результат записывается в список.
		"""
		matrix_result_multiply_number = []
		for element_matrix in self.matrix1:
			result = element_matrix * number
			matrix_result_multiply_number.append(result)

		slice1 = matrix_result_multiply_number[:3]
		slice2 = matrix_result_multiply_number[3:6]
		slice3 = matrix_result_multiply_number[6:]
		pretty_matrix_result_multiply_number = f"\n{slice1}\n{slice2}\n{slice3}"
		
		print(f"\nResult of sum:{pretty_matrix_result_multiply_number}")


	def multiply_matrix_on_matrix(self):
		"""
		Умножает матрицу на матрицу
		"""
		self.any_matrix = self.matrix1.pop(0)  # говнокод
		self.a11_1 = self.matrix1.pop(0)  # Блок елементов 1 матрицы
		self.a12_1 = self.matrix1.pop(0)
		self.a13_1 = self.matrix1.pop(0)
		self.a21_1 = self.matrix1.pop(0)
		self.a22_1 = self.matrix1.pop(0)
		self.a23_1 = self.matrix1.pop(0)
		self.a31_1 = self.matrix1.pop(0)
		self.a32_1 = self.matrix1.pop(0)
		self.a33_1 = self.matrix1.pop(0)

		self.any_matrix = self.matrix2.pop(0)  # говнокод
		self.a11_2 = self.matrix2.pop(0)  # Блок елементов 2 матрицы
		self.a12_2 = self.matrix2.pop(0)
		self.a13_2 = self.matrix2.pop(0)
		self.a21_2 = self.matrix2.pop(0)
		self.a22_2 = self.matrix2.pop(0)
		self.a23_2 = self.matrix2.pop(0)
		self.a31_2 = self.matrix2.pop(0)
		self.a32_2 = self.matrix2.pop(0)
		self.a33_2 = self.matrix2.pop(0)

		a11_res = (self.a11_1 * self.a11_2) + (self.a12_1 * self.a21_2) + (self.a13_1 * self.a31_2)
		a12_res = (self.a11_1 * self.a12_2) + (self.a12_1 * self.a22_2) + (self.a13_1 * self.a32_2)
		a13_res = (self.a11_1 * self.a13_2) + (self.a12_1 * self.a23_2) + (self.a13_1 * self.a33_2)
		
		a21_res = (self.a21_1 * self.a11_2) + (self.a22_1 * self.a21_2) + (self.a23_1 * self.a31_2)
		a22_res = (self.a21_1 * self.a12_2) + (self.a22_1 * self.a22_2) + (self.a23_1 * self.a32_2)
		a23_res = (self.a21_1 * self.a13_2) + (self.a22_1 * self.a23_2) + (self.a23_1 * self.a33_2)
		
		a31_res = (self.a31_1 * self.a11_2) + (self.a32_1 * self.a21_2) + (self.a33_1 * self.a31_2)
		a32_res = (self.a31_1 * self.a12_2) + (self.a32_1 * self.a22_2) + (self.a33_1 * self.a32_2)
		a33_res = (self.a31_1 * self.a13_2) + (self.a32_1 * self.a23_2) + (self.a33_1 * self.a33_2)

		matrix_result_multiply_matrix = [a11_res, a12_res, a13_res, a21_res, 
									a22_res, a23_res, a31_res, a32_res, a33_res]
		slice1 = matrix_result_multiply_matrix[:3]
		slice2 = matrix_result_multiply_matrix[3:6]
		slice3 = matrix_result_multiply_matrix[6:]
		pretty_matrix_result_multiply_matrix = f"\n{slice1}\n{slice2}\n{slice3}"
		print(f"\nResult of sum:{pretty_matrix_result_multiply_matrix}")



def input_matrix(matrix_number):
	"""
	Принимает номер матрицы как параметр, через инпут принимает элементы 
	матрицы, заносит все это в список и возвращает этот список
	"""
	print(f"Input your {matrix_number} 3x3 like this:")  # Ввод 1 матрици 
	print("№1 №2 №3 \n№4 №5 №6 \n№7 №8 №9")
	mtrx1 = int(input("Enter your №1:  "))
	mtrx2 = int(input("Enter your №2:  "))
	mtrx3 = int(input("Enter your №3:  "))
	mtrx4 = int(input("Enter your №4:  "))
	mtrx5 = int(input("Enter your №5:  "))
	mtrx6 = int(input("Enter your №6:  "))
	mtrx7 = int(input("Enter your №7:  "))
	mtrx8 = int(input("Enter your №8:  "))
	mtrx9 = int(input("Enter your №9:  "))
	matrix_local_list = [matrix_number, mtrx1, mtrx2, mtrx3, mtrx4, 
				mtrx5, mtrx6, mtrx7, mtrx8, mtrx9]
	return matrix_local_list


def create_matrix():
	"""Функция ввода данных матриц"""
	while True:
		print ("\n\n\t\t\tMath Matrices Calculator by Hocuda")
		print ("What you want to do with matrices?")
		answer = input("Sum matrixes - enter '1', " +
						"multiply matrixes - enter '2', quit - 'q': ")
		enter = answer.lower()

		if enter == '1':
			print("You choose sum 3x3 matrices")
			matrix1_list = input_matrix('first matrix')
			print(f"Here is your first matrix \n{matrix1_list}")

			matrix2_list = input_matrix('second matrix')
			print(f"\nHere is your first and second matrices" +
				f"\n{matrix1_list} \t\n{matrix2_list}")
			main = Matrix3x3(matrix1_list, matrix2_list)
			main.sum_matrices()
		
		elif enter == '2':  # Подраздел для умножения матриц 
			print("\nYou choose multiply 3x3 matrices")
			print("What exactly do you want to do?")
			choise = input("Multiply matrix on number - enter '1',\n" +
							"Multiply matrix on matrix - 2, quit - 'q': ")
			true_choise = choise.lower  # !!!!!!!!!!
			
			if choise == '1':  # Если выбранно умножить матрицу на число
				print("You choose multiply matrix on number")
				matrix1_list = input_matrix('matrix')
				print(f"Here is your matrix \n{matrix1_list}")
				
				number = input("Number which the matrix will be multiplied: ")
				main = Matrix3x3(matrix1_list)
				main.multiply_matrix_on_numbers(int(number))

			elif choise == '2':  # Если выбранно умножить матрицу на матрицу
				print("You choose multiply matrix on matrix")
				matrix1_list = input_matrix('first matrix')
				print(f"Here is your first matrix \n{matrix1_list}")

				matrix2_list = input_matrix('second matrix')
				print(f"\nHere is your first and second matrices" +
					f"\n{matrix1_list} \t\n{matrix2_list}")
				main = Matrix3x3(matrix1_list, matrix2_list)
				main.multiply_matrix_on_matrix()

			elif choise == 'q' or choise == 'quit' or choise == 'й':
				break


		elif enter == 'q' or enter == 'quit' or enter == "й":
			break
		else:
			print("\nWhat? Try again")

create_matrix()