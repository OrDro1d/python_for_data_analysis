weird_text = input().split()
right_words = []
for i in range(0, len(weird_text)):
    for j in range(0, len(weird_text)):
        if i != j and weird_text[i] == weird_text[j]:
            for k in range(0, len(right_words)):
                if weird_text[i] == right_words[k]:
                    break
            else:
                right_words.append(weird_text[i])
right_words.sort()
print(*right_words)
