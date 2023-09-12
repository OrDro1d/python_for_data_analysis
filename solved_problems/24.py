def wave(size, num, last_num=-1):
    for i in range(2, size):
        for j in range(0, i):
            print(num, end=' ')
            if num == last_num and last_num != -1:
                return 0
            num += 1
        print()
    for i in range(size, 1, -1):
        for j in range(0, i):
            print(num, end=' ')
            if num == last_num and last_num != -1:
                return 0
            num += 1
        print()
    print(num)
    num += 1
    return num


def wave_builder(last_num):
    size, num = 2, 1
    print(num)
    num += 1
    while True:
        num = wave(size, num, last_num)
        if num == 0:
            return 0
        size += 1


N = int(input())
wave_builder(N)
