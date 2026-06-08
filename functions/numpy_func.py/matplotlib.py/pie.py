import matplotlib.pyplot as plt
products = ['A', 'B', 'C', 'D', 'E ']
sales = [100, 150, 80, 120, 90]
plt.pie(sales, labels=products, autopct='%1.1f%%')
plt.title("Sales Distribution")
plt.show()