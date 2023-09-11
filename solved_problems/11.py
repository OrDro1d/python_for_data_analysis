a, b, c = map(int, input().split())
if abs(a - b) <= abs(a - c):
    print("B", abs(a - b))
else:
    print("C", abs(a - c))
