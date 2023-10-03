import numpy as np

n, m, target = map(int, input().split())
arr = np.array(list([input().split() for i in range(0, n)]), dtype=int)

arr_mask = arr % 2 == 0
arr[arr_mask] = target

[print(*arr[i]) for i in range(0, len(arr))]
