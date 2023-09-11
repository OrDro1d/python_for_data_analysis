low, high = map(int, input().split())
counter = 0
for i in range(low, high + 1):
    if i % 2 == 1:
        counter += 1
print(counter)
