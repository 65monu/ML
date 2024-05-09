import numpy as np
#Single Dimensional Array 
a = ['A', 1, "TOM",9.54,0] 
print("Single dimensional array: \n", a)
# Multi-Dimensional Array 
b = [[1, 3, 5], [8, 5, 6], [7, 1, 6]] 
print("\nMulti-Dimensional array: \n", b)
# Array with all ones
C = np.ones (5, dtype = int) 
print("\nArray with all ones: \n", c)
# Array with all zeros
d = np.zeros(6)
print("\nArray with all zeros: \n", d)
# Array with random Values
e = np.random.randint(1,100, size = 10) #range (1,100)
print("\nArray with randome values: \n", e)
# Diagonal Matrix
diag_el = np.array ([1,7,2,3])
f = np.diag(diag_el)
print("\nDiagonal Matrix: \n", f)