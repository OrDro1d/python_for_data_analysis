import numpy as np

arr = np.array(input().split(), dtype=int)
bool_arr = arr > 127

for i in range(0, len(arr)):
    if bool_arr[i]:
        arr[i] = 1
    else:
        arr[i] = 0

print(*arr)
