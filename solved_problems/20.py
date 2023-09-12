n, old_users, k, new_users = int(input()), input().split(), int(input()), input().split()
unique_users = []
for i in range(0, len(new_users)):
    for j in range(0, len(old_users)):
        if new_users[i] == old_users[j]:
            break
    else:
        for k in range(0, len(unique_users)):
            if new_users[i] == unique_users[k]:
                break
        else:
            unique_users.append(new_users[i])
unique_users.sort()
print(*unique_users)
