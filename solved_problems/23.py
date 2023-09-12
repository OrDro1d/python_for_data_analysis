row, col = map(int, input().split())

print("    |", end='')
[print(str(i).rjust(4), end='') for i in range(1, col + 1)]
print("\n   --", end='')
[print("----", end='') for i in range(1, col + 1)]

for i in range(1, row + 1):
    print()
    print(f"{i}|".rjust(5), end='')
    for j in range(1, col + 1):
        print(str(j * i).rjust(4), end='')
