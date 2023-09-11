length, data = int(input()), list(map(float, input().split()))
smooth_data = []
for i in range(0, length):
    if i == 0 or i == length - 1:
        smooth_data.append(data[i])
    else:
        smooth_data.append((data[i - 1] + data[i] + data[i + 1]) / 3)
print(*smooth_data)