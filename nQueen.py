def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def n_queens(board, row, n, ans):
    if row == n:
        ans.append(board[:])
        return

    for col in range(n):
        if is_safe(board, row, col, n):

            row_list = list(board[row])
            row_list[col] = 'Q'
            board[row] = ''.join(row_list)

            n_queens(board, row + 1, n, ans)

            row_list[col] = '*'
            board[row] = ''.join(row_list)


def solve_n_queens(n):
    board = ['*' * n for _ in range(n)]
    ans = []
    n_queens(board, 0, n, ans)
    return ans

solutions = solve_n_queens(4)
count = 0
for sol in solutions:
    count += 1
    print(f"\nSolution {count}:")
    for row in sol:
        print(row)

print(f"\nTotal solving ways: {count}")
