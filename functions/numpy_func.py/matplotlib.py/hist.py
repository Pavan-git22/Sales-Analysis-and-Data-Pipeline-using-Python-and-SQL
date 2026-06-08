import matplotlib.pyplot as plt
scores = [85, 90, 78, 92, 88 , 95, 80, 91, 87, 89]
plt.hist(scores, bins=5, edgecolor='black')
plt.title("Distribution of Scores")
plt.xlabel("Score Range")
plt.ylabel("Frequency")
plt.show()
