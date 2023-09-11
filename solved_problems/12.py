a, b, c = input().split()
if a == "Нет":
    if b == "Нет":
        if c == "Нет":
            print("Кот")
        else:
            print("Жираф")
    else:
        if c == "Нет":
            print("Курица")
        else:
            print("Страус")
else:
    if b == "Нет":
        if c == "Нет":
            print("Делфин")
        else:
            print("Плезиозавры")
    else:
        if c == "Нет":
            print("Пингвин")
        else:
            print("Утка")