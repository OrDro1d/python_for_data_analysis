import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

fig, ax = plt.subplots()
x = np.array([1, 2, 3, 4, 5, 6, 7], dtype=int)
y = x * (-12 + 2.4) / 7 - 2.4#
ax.plot(x, y, color='blue', marker='^', label='o = 0.1')
y = x * (-6 + 1.5) / 7 - 1.5
ax.plot(x, y, color='green', marker='v', label='o = 0.5')
y = x * (-3 + 1.4) / 7 - 1.4
ax.plot(x, y, color='red', marker='s', label='o = 0.9')
ax.set_xlim(1, 8)
ax.set_ylim(-13, -1)
formatter1 = ticker.FormatStrFormatter("1.0e%d")
ax.yaxis.set_major_formatter(formatter1)
plt.xlabel("Highest Degree of Polynomials P")
plt.ylabel("L2 error")
plt.title('Convergence plot')
plt.legend(loc='lower left')
plt.show()
