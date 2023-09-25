row, col = [int(i) for i in input().split()]
rows, _ = [int(i) for i in input().split()]
maze = [list(input()) for line in range(0, rows)]
aaa = 0


def is_can_exit_from_maze(m, r, c, p_r=-1, p_c=-1):
    global aaa
    print(f"Call №{aaa}", r, c)
    aaa += 1

    if p_r != r - 1 >= 0:
        if m[r - 1][c] == 'E':
            return True
        elif m[r - 1][c] == ' ':
            if is_can_exit_from_maze(m, r - 1, c, r, c):
                return True

    if p_c != c + 1 <= len(m[0]) - 1:
        if m[r][c + 1] == 'E':
            return True
        elif m[r][c + 1] == ' ':
            if is_can_exit_from_maze(m, r, c + 1, r, c):
                return True

    if p_r != r + 1 <= rows - 1:
        if m[r + 1][c] == 'E':
            return True
        elif m[r + 1][c] == ' ':
            if is_can_exit_from_maze(m, r + 1, c, r, c):
                return True

    if p_c != c - 1 >= 0:
        if m[r][c - 1] == 'E':
            return True
        elif m[r][c - 1] == ' ':
            if is_can_exit_from_maze(m, r, c - 1, r, c):
                return True

    return False


[print(maze[i]) for i in range(0, rows)]
if __name__ == "__main__":
    print("YES" if is_can_exit_from_maze(maze, row, col) else "NO")
