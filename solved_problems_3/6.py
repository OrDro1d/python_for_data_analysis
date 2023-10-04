import numpy as np
from math import log

rows, cols = map(int, input().split())
arr = np.array([input().split() for _ in range(0, rows)], dtype=int)

idf = np.array([0] * cols, dtype=float)

for i in range(0, cols):
    nt = 1
    for j in range(0, rows):
        if arr[j][i] != 0:
            nt += 1
    idf[i] = round(log(rows / nt) + 1, 2)

print(*idf)
