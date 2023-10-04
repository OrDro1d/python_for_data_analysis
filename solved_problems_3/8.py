import numpy as np
from math import sin

arr = np.array(input().split(), dtype=float)

print(round(np.array(list(map(sin, arr ** 2))).min(), 2))