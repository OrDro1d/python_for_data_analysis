size, heights = int(input()), list(map(int, input().split()))
water, point, step, local_height, flag = 0, 0, 0, 0, False
while True:
    if heights[point + 1] < heights[point]:
        local_height = heights[point]
        for i in range(point + 1, size):
            if heights[i] >= local_height:

        else:
            water += local_height - heights[i]
print(water)
