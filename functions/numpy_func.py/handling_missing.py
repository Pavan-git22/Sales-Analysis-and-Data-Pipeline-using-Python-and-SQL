import numpy as np
arr = np.array([1,2,np.nan])
print(np.isnan(arr))

rectified_arr = np.nan_to_num(arr, nan=10)
print(rectified_arr)

arr1 = np.array([1,2,3 , np.inf, -np.inf])
print(np.isinf(arr1))
cleaned_arr1 = np.nan_to_num(arr1, nan=0, posinf=100, neginf=-100)
print(cleaned_arr1)