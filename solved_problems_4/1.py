import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker

fig, ax = plt.subplots()
x, y = [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]
ax.plot(x, y, color='blue', marker='^', label='o = 0.1')
y = [1.0E-2, 1.0E-4, 1.0E-6, 1.0E-6, 1.0E-9, 1.0E-10, 1.0E-12]
ax.plot(x, y, color='red', marker='o', label='o = 0.9')
y = [1.0E-1, 1.0E-1, 1.0E-2, 1.0E-2, 1.0E-2, 1.0E-2, 1.0E-3]
ax.plot(x, y, color='red', marker='>', label='o = 0.5')
ax.set_xlim(1, 8)
ax.set_ylim(1.0E-13, 1.0E-1)
ax.yaxis.set_major_locator(ticker.FixedLocator(np.linspace(1.0E-13, 1.0E-1, 7)))
plt.xlabel("Highest Degree of Polynomials P")
plt.ylabel("L2 error")
plt.title('Convergence plot')
plt.legend(loc='lower left')
plt.show()
