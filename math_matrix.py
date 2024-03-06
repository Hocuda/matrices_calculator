class Matrix_3х3:

	def __init__(self, matrix_name, a11, a21, a31, a12, a22, a32, a13, a23, a33):
		self.a11 = int(a11)  # Блок для елементов матриц
		self.a21 = int(a21)
		self.a31 = int(a31)
		self.a12 = int(a12)
		self.a22 = int(a22)
		self.a32 = int(a32)
		self.a13 = int(a13)
		self.a23 = int(a23)
		self.a33 = int(a33)

		self.i_1_list = [a11, a21, a31]  # Блок списков для рядов в матрице
		self.i_2_list = [a12, a22, a32]
		self.i_3_list = [a13, a23, a33]
		
		self.matrix_name = matrix_name
		self.matrix_list = [self.a11, self.a21, self.a31, self.a12, self.a22,
							 self.a32, self.a13, self.a23, self.a33]

	def str(self):
		return f"{self.matrix_name.title()} =\n\t\t{self.i_1_list}\n\t\t{self.i_2_list}\n\t\t{self.i_3_list}" # Выводит отформатированую матрицу, сделаную из рядов

	def list(self): #  Матрица одной строкой 
		return (self.matrix_list)


class Matrix_sum(Matrix_3х3):

	def __init__(self, matrix_1, matrix_2): # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		super().__init__(matrix_sum,  matrix_1.a11, matrix_1.a21, matrix_1.a31,
                         matrix_1.a12, matrix_1.a22, matrix_1.a32,
                         matrix_1.a13, matrix_1.a23, matrix_1.a33)
		self.matrix_1 = matrix_1
		self.matrix_2 = matrix_2
		return_sum = []
		self.return_sum = return_sum

	def matrix_sum(self):
		for a, b in self.matrix_1, self.matrix_2:
			a = self.matrix_1.pop(0)
			b = self.matrix_2.pop(0)
			c = a + b
			return_sum.append(c)
		return return_sum

"""matrix1 = Matrix_3х3('matrix1', 1, 0 ,0, 0, 1, 0, 0, 0, 1)
matrix2 = Matrix_3х3('matrix2', 0, 1, 1, 1, 0, 1, 1, 1, 0)

matrix1.str()
matrix2.str()

print (matrix1.list())  # Что-то вроде теста для класса(подтверждение работы)
print (matrix2.list())

matrix_sum_val = Matrix_sum(matrix1, matrix2)
print (matrix_sum_val.matrix_sum()) """

while True:
	print ("\n\t\t\tMath Matrix Calculator by hocuda")
	print ("What you want to do with your matrix?")
	enter = input ("Sum matrixes - enter '1',multiply matrixes enter '2', quit - 'q':")
	
	if enter.lower() == '1':
		print ("You choose sum 3x3 matrix")
		print ("Input your first 3x3 matrix like this:")  # Ввод 1 матрици 
		print ("№1 №2 №3 \n№4 №5 №6 \n№7 №8 №9")
		mtrx1 = input ("Enter your №1:  ")
		mtrx2 = input ("Enter your №2:  ")
		mtrx3 = input ("Enter your №3:  ")
		mtrx4 = input ("Enter your №4:  ")
		mtrx5 = input ("Enter your №5:  ")
		mtrx6 = input ("Enter your №6:  ")
		mtrx7 = input ("Enter your №7:  ")
		mtrx8 = input ("Enter your №8:  ")
		mtrx9 = input ("Enter your №9:  ")
		matrix1 = Matrix_3х3('matrix1', mtrx1, mtrx2, mtrx3, mtrx4, 
								mtrx5, mtrx6, mtrx7, mtrx8, mtrx9)
		print (f"Here is your first matrix \n{matrix1.str()}")

		print ("Input your second 3x3 matrix like this:")  # Ввод 2 матрици 
		print ("№1 №2 №3 \n№4 №5 №6 \n№7 №8 №9")
		mtrx1_2 = int(input("Enter your №1:  "))
		mtrx2_2 = int(input("Enter your №2:  "))
		mtrx3_2 = int(input("Enter your №3:  "))
		mtrx4_2 = int(input("Enter your №4:  "))
		mtrx5_2 = int(input("Enter your №5:  "))
		mtrx6_2 = int(input("Enter your №6:  "))
		mtrx7_2 = int(input("Enter your №7:  "))
		mtrx8_2 = int(input("Enter your №8:  "))
		mtrx9_2 = int(input("Enter your №9:  "))
		matrix2 = Matrix_3х3('matrix2', mtrx1_2, mtrx2_2, mtrx3_2, mtrx4_2, 
								mtrx5_2, mtrx6_2, mtrx7_2, mtrx8_2, mtrx9_2)
		print (f"\nHere is your first and second matrix \n{matrix1.str()} \t\n{matrix2.str()}")
		back = Matrix_sum(matrix1, matrix2)
		sum_of_matrixes = back.matrix_sum()
		print (sum_of_matrixes)

	elif enter.lower() == '2':
		print ("Coming soon")
	elif enter.lower() == "q" or "quit":
		break
	else:
		print (f"{enter} is not in menu")
		continue