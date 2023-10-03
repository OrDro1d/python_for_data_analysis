import numpy as np

rows, cols = map(int, input().split())
arr = np.array(list(input().split() for i in range(0, rows)), dtype=int)

FILTER = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]], dtype=int)
result_arr = np.empty((rows - 2, cols - 2), dtype=int)

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        result_arr[i - 1][j - 1] = (arr[i - 1:i + 2, j-1:j+2] * FILTER).sum()

result_arr_mask = result_arr < 0
result_arr[result_arr_mask] = 0

result_arr_mask = result_arr > 255
result_arr[result_arr_mask] = 255

[print(*result_arr[i]) for i in range(0, rows - 2)]
