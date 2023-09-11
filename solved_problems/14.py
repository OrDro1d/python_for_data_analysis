length, numbers = int(input()), list(map(int, input().split()))
unique_numbers, counter = [], 0
for i in range(0, length):
    for j in range(0, len(unique_numbers)):
        if numbers[i] == unique_numbers[j]:
            break
    else:
        unique_numbers.append(numbers[i])
        counter += 1
print(counter)
