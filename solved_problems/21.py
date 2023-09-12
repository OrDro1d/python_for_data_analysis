number, numbers = int(input()), list(map(int, input().split()))
frequency = [0 for i in range(0, number)]
for i in range(0, number):
    for j in range(0, number):
        if i != j and numbers[i] == numbers[j]:
            frequency[i] += 1
print(numbers[frequency.index(max(frequency))])
