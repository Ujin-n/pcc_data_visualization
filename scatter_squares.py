import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=10)

# Set char title and label axes.
plt.title("Square numbers", fontsize=22)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Square of Value", fontsize=12)

# Set the range for each axis.
plt.axis([0, 1100, 0, 1000000])

plt.show()
