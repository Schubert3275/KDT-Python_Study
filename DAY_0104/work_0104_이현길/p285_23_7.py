"""
23.7 심사문제: 지뢰찾기
"""
col, row = map(int, input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))
# col, row = 3, 3
# matrix = [['.', '*', '*'],
#           ['*', '.', '.'],
#           ['.', '*', '.']]
# col, row = 5, 5
# matrix = [['.', '.', '*', '.', '.'],
#           ['.', '.', '.', '*', '.'],
#           ['.', '*', '.', '.', '.'],
#           ['.', '*', '*', '*', '.'],
#           ['*', '.', '*', '.', '.']]
matrix_result = [[0 for i in range(row)] for j in range(col)]
for i in range(col):
    for j in range(row):
        if matrix[i][j] == '*':
            matrix_result[i][j] = '*'
        elif matrix[i][j] == '.':
            for x, y in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                if i + x < 0 or i + x > col - 1:
                    continue
                if j + y < 0 or j + y > row - 1:
                    continue
                if matrix[i + x][j + y] == '*':
                    matrix_result[i][j] += 1
for i in range(col):
    for j in range(row):
        print(matrix_result[i][j], end='')
    print()
