#addition, subtraction, multiplication
import numpy as np
a = np.array([ [1, 2, 3],[4, 5, 6],[7, 8, 9] ])
b = np.array([ [1, 3, 5],  [8, 5, 6], [7, 1, 6]])
print("Matrix a = ")
print(a)
print("\nMatrix b = ")
print(b)
print("\nMatrix Additon = ")
print(np.add(a,b))
print("\nMatrix subtraction = ") 
print(np.subtract(a,b))
print("\nMatrix Multiplication = ") 
print(np.dot(a,b), "\n")

# display specific rows or columns of the matrix. 
print('first row of matrix a :') 
print (a[0])
print('third row of matrix a :') 
print (a[2])
print('second column of matrix b :') 
print (b[:,1])