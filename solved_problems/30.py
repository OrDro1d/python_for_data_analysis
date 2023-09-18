file = open('input.txt', 'r', encoding='utf-8')
text = list(map(str.strip, file.readlines()))
words = []
for line in text:
    words = line.split()
file.close()
eng_words = ['They', 'they', 'the', 'The', 'we', 'We', "Is", 'is', 'are', "are"]
for word in words:
    if word in eng_words:
        print("EN")
        break
else:
    print("RUS")
