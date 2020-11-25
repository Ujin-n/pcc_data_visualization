import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.plot(input_values, squares, linewidth=4)

# Set chart title and label axes.
plt.title("Square numbers", fontsize=22)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Square of Value", fontsize=12)

# Set size of tick labels.
plt.tick_params(axis='both', labelsize=12)


plt.show()
