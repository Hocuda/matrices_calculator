class Matrix3x3:
	"""
	Класс для математический действий с матрицами 
	//иногда 'm' это сокращенно matrix а 'n' это number
	"""
	def __init__(self, matrix1=None, matrix2=None):
		"""
		Функция инициализации класса. По дефолту стоят None для функции
		multiply_matrix_on_number, где используеться только одна матрица
		"""
		self.matrix1 = matrix1
		self.matrix2 = matrix2

	def sum_m(self):
		"""
		Принимает и записывает элементы в списки с номером матрицы, потом через
		цикл вырезает из каждого списка 1 элемент и после сумма этих елементов
		записывается в конец нового списка с результатами. После этого список с
		результатами нарезаеться на 3 списка для красивого вывода.
		"""
		matrix_result_sum = []
		for matrix_result in range(9):
			matrix1_for = self.matrix1.pop(0)
			matrix2_for = self.matrix2.pop(0)
			matrix_result = matrix1_for + matrix2_for
			matrix_result_sum.append(matrix_result)

		slice1 = matrix_result_sum[:3]
		slice2 = matrix_result_sum[3:6]
		slice3 = matrix_result_sum[6:]
		pretty_matrix_result = f"\n{slice1}\n{slice2}\n{slice3}"

		return pretty_matrix_result

	def multiply_m_on_n(self, number):
		"""
		Умножает матрици на числа. Каждый элемент матрици умножается на
		введенное число и результат записывается в список. После этого список с
		результатами нарезаеться на 3 списка для красивого вывода.
		"""
		m_result_multiply_n = []
		for element_matrix in self.matrix1:
			result = element_matrix * number
			m_result_multiply_n.append(result)

		slice1 = m_result_multiply_n[:3]
		slice2 = m_result_multiply_n[3:6]
		slice3 = m_result_multiply_n[6:]
		pretty_matrix_result = f"\n{slice1}\n{slice2}\n{slice3}"

		return pretty_matrix_result

	def multiply_m_on_m(self):
		"""
		Умножает матрицу на матрицу. Много некрасивого кода, не знаю как это
		оптимизировать. Переменные, в которых есть _res это элементы финальной
		матрицы, которые вычисляються по аглоритму. После этого список с
		результатами нарезаеться на 3 списка для красивого вывода.
		"""
		self.a11_1 = self.matrix1.pop(0)  # Блок определения элементов 1 матрицы
		self.a12_1 = self.matrix1.pop(0)
		self.a13_1 = self.matrix1.pop(0)
		self.a21_1 = self.matrix1.pop(0)
		self.a22_1 = self.matrix1.pop(0)
		self.a23_1 = self.matrix1.pop(0)
		self.a31_1 = self.matrix1.pop(0)
		self.a32_1 = self.matrix1.pop(0)
		self.a33_1 = self.matrix1.pop(0)

		self.a11_2 = self.matrix2.pop(0)  # Блок определения элементов 2 матрицы
		self.a12_2 = self.matrix2.pop(0)
		self.a13_2 = self.matrix2.pop(0)
		self.a21_2 = self.matrix2.pop(0)
		self.a22_2 = self.matrix2.pop(0)
		self.a23_2 = self.matrix2.pop(0)
		self.a31_2 = self.matrix2.pop(0)
		self.a32_2 = self.matrix2.pop(0)
		self.a33_2 = self.matrix2.pop(0)
 		  # Алгоритм для умножения матриц
		a11_res = (self.a11_1 * self.a11_2) + (self.a12_1 * self.a21_2) + (self.a13_1 * self.a31_2)
		a12_res = (self.a11_1 * self.a12_2) + (self.a12_1 * self.a22_2) + (self.a13_1 * self.a32_2)
		a13_res = (self.a11_1 * self.a13_2) + (self.a12_1 * self.a23_2) + (self.a13_1 * self.a33_2)

		a21_res = (self.a21_1 * self.a11_2) + (self.a22_1 * self.a21_2) + (self.a23_1 * self.a31_2)
		a22_res = (self.a21_1 * self.a12_2) + (self.a22_1 * self.a22_2) + (self.a23_1 * self.a32_2)
		a23_res = (self.a21_1 * self.a13_2) + (self.a22_1 * self.a23_2) + (self.a23_1 * self.a33_2)

		a31_res = (self.a31_1 * self.a11_2) + (self.a32_1 * self.a21_2) + (self.a33_1 * self.a31_2)
		a32_res = (self.a31_1 * self.a12_2) + (self.a32_1 * self.a22_2) + (self.a33_1 * self.a32_2)
		a33_res = (self.a31_1 * self.a13_2) + (self.a32_1 * self.a23_2) + (self.a33_1 * self.a33_2)

		m_result_multiply_m = [a11_res, a12_res, a13_res, a21_res, 
									a22_res, a23_res, a31_res, a32_res, a33_res]
		slice1 = m_result_multiply_m[:3]
		slice2 = m_result_multiply_m[3:6]
		slice3 = m_result_multiply_m[6:]
		pretty_matrix_result = f"\n{slice1}\n{slice2}\n{slice3}"

		return pretty_matrix_result

	def transpose_m(self):
		"""Транспонирование матрицы"""
		m1 = self.matrix1
		slice1 = [m1[0], m1[3], m1[6]]
		slice2 = [m1[1], m1[4], m1[7]]
		slice3 = [m1[2], m1[5], m1[8]]
		pretty_matrix_result = f"\n{slice1}\n{slice2}\n{slice3}"
		return pretty_matrix_result

			

def input_matrix(matrix_number):
	"""
	Через инпут в цикле принимает элементы матрицы, если введены строки - список
	очищаеться и цикл for стартует заново из-за цикла While, если введенная
	строка 'q' или 'quit' цикл for и While завершаться. Если длина списка равна
	или больше 9 - функция ретурнет список и завершиться.
	"""
	print(f"Input your {matrix_number} 3x3 like this:") 
	print("№1 №2 №3 \n№4 №5 №6 \n№7 №8 №9")
	
	matrix_local_list = []

	q = True
	while q:
		for i in range(9):
			x = i+1
			element = input(f"Enter your №{x}:  ")

			try:
				if element.lower() == 'q' or element.lower() == 'quit':
					q = False
					break
				matrix_local_list.append(int(element))
			except ValueError:
				print("Its not number, try again")
				matrix_local_list.clear()
				break
			else:
				if len(matrix_local_list) >= 9:
					return matrix_local_list
					q = False
					break

def create_matrix():
	"""
	Функция выбора что делать с матрицами. Добавлены блоки if else что бы если
	будет введено 'q' или 'quit' то цикл завершится и программа завершится.
	"""
	print("\n\n                                           __                         ")
	print("|V| _ _|_ |_    |V| _ _|_ __ o  _  _  _   /     _  |  _     |  _ _|_ _  __")
	print("| |(_| |_ | |   | |(_| |_ |  | (_ (/__>   \\__  (_| | (_ |_| | (_| |_(_) | ")
	print("\nby Hocuda")
	while True:
		print("\n\t\t\tWhat you want to do with matrices?")
		enter = input("Sum, transpose matrixes - enter '1', " +
						"multiply matrixes - enter '2', quit - 'q': ")
		if enter == '1':
			print("You choose sum or transpose 3x3 matrices")
			print("What exactly do you want to do?")
			choise = input("Sum matrices - enter '1',\n" +
							"Transpose of a matrix - enter '2' quit - 'q': ")

			if choise == '1':
				print("You choose sum 3x3 matrices")
				matrix1_list = input_matrix('first matrix')
				if matrix1_list:
					pass
				else:
					break

				print(f"Here is your first matrix \n{matrix1_list}")

				matrix2_list = input_matrix('second matrix')
				if matrix2_list:
					pass
				else:
					break

				print(f"\nHere is your first and second matrices" +
					f"\n{matrix1_list} \t\n{matrix2_list}")
				main = Matrix3x3(matrix1_list, matrix2_list)
				pretty_matrix_result = main.sum_m()
				print ("\nResult of sum:", pretty_matrix_result)

			elif choise == '2':
				print("You choose transpose of a matrix")
				matrix1_list = input_matrix('matrix')
				if matrix1_list:
					pass
				else:
					break

				print(f"Here is your first matrix \n{matrix1_list}")
				
				main = Matrix3x3(matrix1_list)
				pretty_matrix_result = main.transpose_m()
				print("\nResult of transpose matrix:", pretty_matrix_result)

			elif choise.lower() == 'q' or choise.lower() == 'quit':
				break
			else:
				print("What? Try again")

		elif enter == '2':  # Подраздел для умножения матриц
			print("\nYou choose multiply 3x3 matrices")
			print("What exactly do you want to do?")
			choise = input("Multiply matrix on number - enter '1',\n" +
							"Multiply matrix on matrix - 2, quit - 'q': ")

			if choise == '1':  # Если выбранно умножить матрицу на число
				print("You choose multiply matrix on number")
				matrix1_list = input_matrix('matrix')
				if matrix1_list:
					pass
				else:
					break

				print(f"Here is your matrix \n{matrix1_list}")

				while True:
					number = input("Number which the matrix will be multiplied: ")
					if number.lower() == 'q' or number.lower() == 'quit':
						break

					try:
						number = int(number)
					except ValueError:
						print("Its not number, try again")
					else:
						main = Matrix3x3(matrix1_list)
						pretty_matrix_result = main.multiply_m_on_n(number)
						print(f"\nResult of sum:", pretty_matrix_result)
						break

			elif choise == '2':  # Если выбранно умножить матрицу на матрицу
				print("You choose multiply matrix on matrix")
				matrix1_list = input_matrix('first matrix')
				if matrix1_list:
					pass
				else:
					break

				print(f"Here is your first matrix \n{matrix1_list}")

				matrix2_list = input_matrix('second matrix')
				if matrix2_list:
					pass
				else:
					break

				print(f"\nHere is your first and second matrices" +
					f"\n{matrix1_list} \t\n{matrix2_list}")
				main = Matrix3x3(matrix1_list, matrix2_list)
				pretty_matrix_result = main.multiply_m_on_m()
				print(f"\nResult of sum:", pretty_matrix_result)

			elif choise.lower() == 'q' or choise.lower() == 'quit':
				break

		elif enter.lower() == 'q' or enter.lower() == 'quit':
			break
		else:
			print("\nWhat? Try again")


if __name__ == '__main__':
	create_matrix()
