n = int(input())

a = n // 5000
n %= 5000

b = n // 1000
n %= 1000

c = n // 500
n %= 500

d = n // 200
n %= 200

e = n // 100
n %= 100

print(a, b, c, d, e)