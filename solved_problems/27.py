n = int(input())
heights = list(map(int, input().split()))

left, right = 0, n - 1
water, current_height = 0, 0

while left < right:
    if heights[left] <= heights[right]:
        if heights[left] > current_height:
            current_height = heights[left]
        else:
            water += current_height - heights[left]
        left += 1
    else:
        if heights[right] > current_height:
            current_height = heights[right]
        else:
            water += current_height - heights[right]
        right -= 1

print(water)
