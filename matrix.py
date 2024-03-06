class Matrix3x3:
	"""
	Цели: Пофиксить вывод после суммирования +
		  Пересмотреть ретурн matrix_logic и вообще весь matrix_logic
		  Добавить другие операции кроме умножения
		  Добавить блоки try exept если в матрицу будут введены буквы
		  Доделать красивый вывод результата суммирования матрици +
		  Сделать отдельную функцию для инпутов элементов матриц +
		  Проработать интерфейс
		  Добавить выход если в инпуте любого числа написать 'q' или 'quit'

	"""
	def __init__(self, matrix1, matrix2):
		"""Функция инициализации класса"""
		self.matrix1 = matrix1
		self.matrix2 = matrix2
		self.matrix_name = [matrix1.pop(0), matrix2.pop(0)]
		self.matrix_list = [self.matrix1, self.matrix2]

	def matrix_logic(self):
		"""
		Вырезает из списка со списками матриц
		первую из них, вырезает из неё элементы 
		в переменные и возвращает список из них
		"""
		self.any_matrix = self.matrix_list.pop(0)
		self.a11 = int(self.any_matrix.pop(0))  # Блок для елементов матриц
		self.a21 = int(self.any_matrix.pop(0))
		self.a31 = int(self.any_matrix.pop(0))
		self.a12 = int(self.any_matrix.pop(0))
		self.a22 = int(self.any_matrix.pop(0))
		self.a32 = int(self.any_matrix.pop(0))
		self.a13 = int(self.any_matrix.pop(0))
		self.a23 = int(self.any_matrix.pop(0))
		self.a33 = int(self.any_matrix.pop(0))

		return_list = [self.any_matrix, self.a11, self.a21, self.a31, self.a12,
						 self.a22, self.a32, self.a13, self.a23, self.a33]
		return return_list

	def sum_matrix(self):
		"""
		Принимает 2 ретурна от matrix_logic и записывает их в списки с номером 
		матрицы, потом через цикл вырезает из каждого списка 2 элемент, 
		потому-что первый это название матрицы и после сумма этих елементов 
		записывается в конец нового списка с результатами. После этого список с 
		результатами нарезаеться на 3 списка для красивого вывода.  
		"""
		matrix1_1 = self.matrix_logic()
		matrix2_2 = self.matrix_logic()
		matrix_result_sum = []
		for matrix_result in range(9):
			matrix1_for = matrix1_1.pop(1)
			matrix2_for = matrix2_2.pop(1)
			matrix_result = matrix1_for + matrix2_for
			matrix_result_sum.append(matrix_result)

		slice_1 = matrix_result_sum[:3]
		slice_2 = matrix_result_sum[3:6]
		slice_3 = matrix_result_sum[6:]
		pretty_matrix_result_sum = f"\n{slice_1} \n{slice_2} \n{slice_3}"

		print ("\nResult of sum:", pretty_matrix_result_sum)


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
		print ("\n\t\t\tMath Matrix Calculator by hocuda")
		print ("What you want to do with your matrix?")
		enter = input ("Sum matrixes - enter '1', quit - 'q':")
		
		if enter == '1':
			print("You choose sum 3x3 matrix")
			matrix1_list = input_matrix('first matrix')
			print(f"Here is your first matrix \n{matrix1_list}")

			matrix2_list = input_matrix('second matrix')
			print(f"\nHere is your first and second matrix \n{matrix1_list} \t\n{matrix2_list}")
			return matrix1_list, matrix2_list

		elif enter == 'q' or enter == 'quit':
			break
		else:
			print("What? Try again")

main_matrix = Matrix3x3(*create_matrix())
main_matrix.sum_matrix()