import numpy as np
matrix = np.array([-1,-2,3,4,5,6,7,8,9,10,11,12]).reshape (4,3) 
print(matrix)
print("Absolute Values of the matrix ") 
print(np.absolute (matrix))
print('Negative of matrix') 
print(np.negative (matrix))

#adding row at the end
print("Add Row")
print(np.append(matrix, [[13,14,15]], axis=0))

#adding row at specified position 
print("Add Row with position")
print(np.insert(matrix, 1, [[16,17,18]], axis=0))

#Adding column at the end
print("Add Column")
print(np.append(matrix, [[19], [20], [21],[22]],axis=1)) 

#removing specified column
print("Remove Column")
print(np.delete(matrix, 1, axis=1))

#removing specified row
print("Remove Row")
print(np.delete(matrix,1,axis=0))

print('maximum element of the matrix', np.max(matrix))

print('minimum element of the matrix', np.min(matrix))

print('sum of elements of the matrix',np.sum(matrix))

print('sum of elements of second row of the matrix', np.sum(matrix[1]))

print('sum of elements of third column of the matrix',np.sum(matrix[:,2]))