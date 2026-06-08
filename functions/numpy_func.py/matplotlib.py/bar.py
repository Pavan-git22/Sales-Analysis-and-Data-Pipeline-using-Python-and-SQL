import matplotlib.pyplot as plt
x = ['mon', 'tue', 'wed', 'thu', 'fri']
y = [10, 20, 30, 40, 50]
plt.bar(x,y,color='blue',label='sales')
plt.title("sales per day")
plt.xlabel("day")
plt.ylabel("sales")
plt.legend()
plt.show()