line = input()
result = ''
for i in range(0, len(line)):
    if result.find(line[i]) == -1:
        num = line.count(line[i])
        if num != 1:
            result += str(line[i]) + str(num)
        else:
            result += str(line[i])
print(result)
