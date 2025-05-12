def solve_n_queens(n):
    board = [-1] * n
    solutions = []

    def is_valid(row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_valid(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions

# Get the solutions
solutions = solve_n_queens(8)

# Print the first solution in the required format
if solutions:
    for i in range(8):
        row = [0] * 8
        row[solutions[0][i]] = 1
        print(row)
