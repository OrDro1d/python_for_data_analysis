row, col = [int(i) for i in input().split()]
rows, _ = [int(i) for i in input().split()]
maze = [list(input()) for line in range(0, rows)]
aaa = 1


def is_can_exit_from_maze(m, r, c, last_rc=None):
    if last_rc is None:
        last_rc = [[r, c]]

    global aaa
    print(f"Call №{aaa}: ", r, c)
    aaa += 1

    for rc in last_rc:
        if rc[0] == r - 1:
            break
    else:
        if r - 1 > 0:  # ВВЕРХ
            if m[r - 1][c] == 'E':
                return True
            elif m[r - 1][c] == ' ':
                last_rc.append([r - 1, c])
                if is_can_exit_from_maze(m, r - 1, c, last_rc=[[r, c]]):
                    return True
    print('№', r, c, last_rc)
    for rc in last_rc:
        if rc[1] == c + 1:
            break
    else:
        if c + 1 < len(m[0]) - 1:  # ВПРАВО
            if m[r][c + 1] == 'E':
                return True
            elif m[r][c + 1] == ' ':
                last_rc.append([r, c + 1])
                if is_can_exit_from_maze(m, r, c + 1, last_rc=[[r, c]]):
                    return True
    print('№', r, c, last_rc)
    for rc in last_rc:
        if rc[0] == r + 1:
            break
    else:
        if r + 1 < rows - 1:  # ВНИЗ
            if m[r + 1][c] == 'E':
                return True
            elif m[r + 1][c] == ' ':
                last_rc.append([r + 1, c])
                if is_can_exit_from_maze(m, r + 1, c, last_rc=[[r, c]]):
                    return True
    print('№', r, c, last_rc)
    for rc in last_rc:
        if rc[1] == c - 1:
            break
    else:
        if c - 1 > 0:  # ВЛЕВО
            if m[r][c - 1] == 'E':
                return True
            elif m[r][c - 1] == ' ':
                last_rc.append([r, c - 1])
                if is_can_exit_from_maze(m, r, c - 1, last_rc=[[r, c]]):
                    return True
    print('№', r, c, last_rc)
    return False


[print(maze[i]) for i in range(0, rows)]
if __name__ == "__main__":
    print("YES" if is_can_exit_from_maze(maze, row, col) else "NO")
