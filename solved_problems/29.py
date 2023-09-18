text = input()
num_dict, alpha_list = dict(), []
for letter in text:
    for j in range(0, len(alpha_list)):
        if alpha_list[j] == letter:
            break
    else:
        alpha_list.append(letter)
        num_dict.setdefault(letter, text.count(letter))
alpha_list.sort()
for i in range(max(num_dict.values()), 0, -1):
    for letter in alpha_list:
        if num_dict.get(letter) >= i:
            print("#", end='')
        else:
            print(" ", end='')
    print()
print(*alpha_list, sep='')
