import matplotlib.pyplot as plt
x = ['mon', 'tue', 'wed', 'thu', 'fri']
y = [10, 20, 30, 40, 50]


# plt.subplot(1, 2, 1)
# plt.plot(x, y)
# plt.title("sales per day")

# plt.subplot(1, 2, 2)
# plt.bar(x,y,color='blue',label='sales')
# plt.title("sales per day")

# plt.xlabel("day")
# plt.ylabel("sales")
# plt.legend()
# plt.show()
fig , ax= plt.subplots(1,2,figsize=(10,5))
ax[0].plot(x, y)
ax[0].set_title("sales per day")

ax[1].bar(x,y)
ax[1].set_title("sales per day")

plt.show()