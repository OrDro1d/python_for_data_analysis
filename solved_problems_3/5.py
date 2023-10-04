import numpy as np

rows, cols = map(int, input().split())
arr = np.array([input().split() for _ in range(0, rows)], dtype=float)

for i in range(0, rows):
    arr[i] = arr[i] / (arr[i] ** 2).sum() ** 0.5
    for j in range(0, cols):
        arr[i][j] = round(arr[i][j], 2)

[print(*arr[i]) for i in range(0, rows)]
