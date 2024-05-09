import numpy as np
import matplotlib.pyplot as plt
import math
plt.hist([1,1, 1, 2, 2, 2, 2, 3, 3,4,5,5,7,7,7])
print(plt.show())
arr = np.array ([1,2,3,4,5,6,7,8,9,10,11,12]).reshape(3,4)
print(arr)
sine_value = [math.sin(i) for i in arr[:,0]]
plt.plot(arr[:,0], sine_value, marker='o')
plt.xlabel('x-axis')
plt.ylabel('sine_values')
print(plt.show())