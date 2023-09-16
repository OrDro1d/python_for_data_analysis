N = int(input())
size, num, flag = 2, 1, False
while True:
    for i in range(1, size):
        for j in range(0, i):
            print(num, end=' ')
            if num == N:
                flag = True
                break
            num += 1
        if flag:
            break
        print()
    if flag:
        break
    for i in range(size, 1, -1):
        for j in range(0, i):
            print(num, end=' ')
            if num == N:
                flag = True
                break
            num += 1
        if flag:
            break
        print()
    if flag:
        break
    size += 1
