weird_text = input().split()
right_words = []
del weird_text[weird_text.index("end"):]
for word in weird_text:
    if weird_text.count(word) > 1 and right_words.count(word) == 0:
        right_words.append(word)
right_words.sort()
print(*right_words)
