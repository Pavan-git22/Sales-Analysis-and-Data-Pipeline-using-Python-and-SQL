import numpy as np
arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15]])
print(arr.shape)
print(arr.size)
print(arr.ndim) #2d array
print(arr.dtype)
float_arr = arr.astype(float)
print(float_arr.dtype)


arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
reshaped_arr = arr.reshape(1, 9) #reshape to 1 row and 9 columns
print(reshaped_arr)