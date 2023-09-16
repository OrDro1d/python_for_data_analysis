num_1, num_2 = input().split()
if len(num_1) == len(num_2):
    for i in range(0, len(num_1)):
        if num_1.count(num_1[i]) != num_2.count(num_1[i]):
            print("NO")
            break
    else:
        print("YES")
else:
    print("NO")
