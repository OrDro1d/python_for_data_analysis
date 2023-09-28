matrix = [[int(i) for i in input()] for _ in range(9)]


def is_valid_sudoku(matrix):
    for mini_square_i in range(0, 3):
        for mini_square_j in range(0, 3):
            for i in range(0, 3):
                for j in range(0, 3):
                    for k in range(0, 9):
                        if ((matrix[i + mini_square_i * 3][j + mini_square_j * 3] == matrix[i + mini_square_i * 3][k]
                            and j + mini_square_j * 3 != k)
                            or (matrix[i + mini_square_i * 3][j + mini_square_j * 3] == matrix[k][j + mini_square_j * 3]
                                and i + mini_square_i * 3 != k)):
                            return False
                        for i1 in range(0, 2):
                            for j1 in range(0, 2):
                                if (matrix[i + mini_square_i * 3][j + mini_square_j * 3] ==
                                    matrix[i1 + mini_square_i * 3][j1 + mini_square_j * 3]
                                        and i + mini_square_i * 3 != j1 + mini_square_j * 3
                                        and j + mini_square_j * 3 != j1 + mini_square_j * 3):
                                    return False
    return True


print('YES' if is_valid_sudoku(matrix) else 'NO')
