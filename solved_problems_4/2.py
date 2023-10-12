import matplotlib.pyplot as plt
fig, ax = plt.subplots()
x, y = [0.02, 0.12, 0.18, 0.36, 0.46, 0.6, 0.55, 0.8, 0.94], [0.78, 0.82, 0.3, 0.68, 0.32, 0.45, 0.6, 0.46, 0.59]
ax.scatter(x, y, color='red', linestyle='-', edgecolors='black', marker='o', label='red')
x, y = [0.14, 0.22, 0.34, 0.44, 0.57, 0.78, 0.86, 0.95, 0.95, 0.98], [0.08, 0.6, 0.24, 0.66, 0.96, 0.5, 0.585, 0.34, -0.04, 0.04]
ax.scatter(x, y, color='green', linestyle='-', edgecolors='black',  marker='o', label='green')
x, y = [0.05, 0.25, 0.34, 0.4, 0.55, 0.62, 0.68, 0.76, 0.9], [0.98, 0.16, 0.32, 0.7, 0.25, 0.45, 0.15, 0.12, 0.75]
ax.scatter(x, y, color='blue', linestyle='-', edgecolors='black',  marker='o', label='blue')
ax.set_xlim(-0.2, 1.2)
ax.set_ylim(-0.2, 1.2)
ax.legend(loc='upper right')
plt.show()
