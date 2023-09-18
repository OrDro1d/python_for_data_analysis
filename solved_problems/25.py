line = input()
result, counter, start_point = '', 1, 1
while True:
    for i in range(start_point, len(line)):
        if line[i] == line[i - 1]:
            counter += 1
            start_point = i + 1
        else:
            if counter == 1:
                result += f"{line[i - 1]}"
                start_point = i + 1
                break
            else:
                result += f"{line[i - 1]}{counter}"
                start_point, counter = i + 1, 1
                break
    else:
        if counter == 1:
            result += f"{line[start_point - 1]}"
            break
        else:
            result += f"{line[start_point - 1]}{counter}"
            break
print(result)
