bioshit = input()
numbers, counter = [], 0
for i in range(0, len(bioshit), 3):
    if (bioshit[i] == 'U' and (bioshit[i + 1] == 'A' and bioshit[i + 2] == 'A'
        or bioshit[i + 1] == 'A' and bioshit[i + 2] == 'G'
        or bioshit[i + 1] == 'G' and bioshit[i + 2] == 'A'
    )):
        numbers.append(counter)
        counter = 0
    else:
        counter += 3
print(*numbers)
