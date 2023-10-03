import numpy as np

arr = np.array(input().split(), dtype=int)
arr_mask = arr > 127

arr[arr_mask] = 1
arr[arr != 1] = 0

print(*arr)
