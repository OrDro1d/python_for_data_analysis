import numpy as np

arr = np.array(input().split(), dtype=int)

[print(i, end=' ') if -100 < arr[i] < 100 else 0 for i in range(0, len(arr))]