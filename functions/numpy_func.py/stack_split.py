import numpy as np

arr1 = np.array([1,2,3,4,5]) 
arr2 = np.array([6,7,8,9,10])
print(np.vstack((arr1, arr2))) #stack along rows
print(np.hstack((arr1, arr2))) #stack along columns

arr1 = np.array([1,2,3,4,5,6])
print(np.split(arr1, 3))

