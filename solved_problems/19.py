average_temp = input().split(';')
sum, length = 0, 0
for i in range(0, len(average_temp)):
    if average_temp[i] != '':
        sum += int(average_temp[i])
        length += 1
print(sum / length)
