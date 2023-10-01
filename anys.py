def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check if there is a queen in the same column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check upper-left diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # Check upper-right diagonal
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True

    def backtrack(board, row):
        if row == n:
            # Found a solution, add it to the results
            solutions.append(["".join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(board, row + 1)
                board[row][col] = '.'  # Backtrack

    solutions = []
    empty_board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(empty_board, 0)
    
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print(row)
        print()

# Example usage:
N = 4
solutions = solve_n_queens(N)
print_solutions(solutions)
