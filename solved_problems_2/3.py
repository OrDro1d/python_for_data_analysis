def sort_key(number):
    counter = 0
    for digit in number:
        if digit == '1':
            counter += 1
    counter **= 10
    lil_counter = 0
    for i in range(0, len(number)):
        if number[i] == '1':
            lil_counter += i
    lil_counter -= len(number) ** 2
    return counter + lil_counter


numbers = input().split()
numbers.sort(reverse=True, key=sort_key)
print(' '.join(numbers))
