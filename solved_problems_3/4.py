import numpy as np

rows, cols = map(int, input().split())
a_array = np.array([input().split() for _ in range(0, rows)], dtype=int)
b_array = np.array([input().split() for _ in range(0, rows)], dtype=int)

msd = ((a_array - b_array) ** 2).sum() / (rows * cols)

print(round(msd, 2))
