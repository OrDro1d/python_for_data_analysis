eng_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num: int = int(input())
word: str = ''
while num > 0:
    if num % 26 == 0:
        word += eng_alpha[25]
        num = num // 26 - 1
        continue
    word += eng_alpha[num % 26 - 1]
    num //= 26
print(word[::-1])
