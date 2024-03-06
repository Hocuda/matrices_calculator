while True:
	print ("\n\t\t\tMath Matrix Calculator by hocuda")
	print ("What you want to do with your matrix?")
	enter = input ("Sum matrixes - enter '1',multiply matrixes enter '2', quit - 'q':")
	
	if enter.lower() == '1':
		print ("You choose sum 3x3 matrix")
		print ("Input your first 3x3 matrix like this:")  # Ввод 1 матрици 
		print ("№1 №2 №3 \n№4 №5 №6 \n№7 №8 №9")
		mtrx1 = int(input("Enter your №1:  "))
		mtrx2 = int(input("Enter your №2:  "))
		mtrx3 = int(input("Enter your №3:  "))
		mtrx4 = int(input("Enter your №4:  "))
		mtrx5 = int(input("Enter your №5:  "))
		mtrx6 = int(input("Enter your №6:  "))
		mtrx7 = int(input("Enter your №7:  "))
		mtrx8 = int(input("Enter your №8:  "))
		mtrx9 = int(input("Enter your №9:  "))
		matrix1 = [mtrx1, mtrx2, mtrx3, mtrx4, 
					mtrx5, mtrx6, mtrx7, mtrx8, mtrx9]
		print (f"Here is your first matrix \n{matrix1}")

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
		matrix2 = [mtrx1_2, mtrx2_2, mtrx3_2, mtrx4_2, 
					mtrx5_2, mtrx6_2, mtrx7_2, mtrx8_2, mtrx9_2]
		print (f"\nHere is your first and second matrix \n{matrix1} \t\n{matrix2}")
		
		matrix_result_sum = []

		for matrix_element_sum in range(9):
			matrix_1 = matrix1.pop(0)
			matrix_2 = matrix2.pop(0)
			matrix_element_sum = matrix_1 + matrix_2
			matrix_result_sum.append(matrix_element_sum)

		print(f"\nHere is your result sum of your matrix:")
		print(matrix_result_sum)
	elif enter.lower() == 'q' or enter.lower() == 'quit':
		break