word = input()
for i in range(0, len(word) // 2):
    if word[i] != word[len(word) - i - 1].upper() and word[i] != word[len(word) - i - 1].lower():
        print("NO")
        break
else:
    print("YES")
