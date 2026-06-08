import matplotlib.pyplot as plt
hours = [1, 2, 3, 4, 5]
sales = [10, 20, 30, 40, 50]
plt.scatter([1,2,3], [10,20,30], color='red', label='sales1')
plt.scatter([4,5], [40,50], color='blue', label='sales2')
plt.title("sales per hour")
plt.xlabel("hour")
plt.ylabel("sales")
plt.grid(True)
plt.legend()
plt.show()