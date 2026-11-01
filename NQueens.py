"""
N-Queens Problem using Backtracking with First Queen Pre-placed.
Prints the matrix at each try (placement & backtracking step).
Time Complexity: O(N!) in worst case.
Space Complexity: O(N^2) for board representation.
"""

def print_board(board, n):
    """Prints the chessboard matrix."""
    for row in board:
        for val in row:
            print(val, end="\t")
        print()
    print("-------------------------------------------------")


def is_safe(board, row, col, n):
    """
    Checks if a queen can be safely placed at board[row][col].
    Checks current row, current column, and all 4 diagonal directions.
    """
    # Check row and column
    for i in range(n):
        if board[row][i] == 1 or board[i][col] == 1:
            return False

    # Check all 4 diagonal directions
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        while 0 <= r < n and 0 <= c < n:
            if board[r][c] == 1:
                return False
            r += dr
            c += dc

    return True


step = 1

def solve_nqueens(board, row_idx, remaining_rows, n):
    """
    Uses backtracking to place queens in the remaining rows,
    printing the matrix at each attempt and backtrack.
    """
    global step

    # Base Case: all remaining queens are placed
    if row_idx == len(remaining_rows):
        return True

    current_row = remaining_rows[row_idx]

    for col in range(n):
        if is_safe(board, current_row, col, n):
            # Place queen
            board[current_row][col] = 1
            print(f"\nStep {step}: [TRY / PLACE] Queen placed at Row {current_row + 1}, Column {col + 1}")
            step += 1
            print_board(board, n)

            # Recur to place queen in next remaining row
            if solve_nqueens(board, row_idx + 1, remaining_rows, n):
                return True

            # Backtrack
            board[current_row][col] = 0
            print(f"\nStep {step}: [BACKTRACK] Removed Queen from Row {current_row + 1}, Column {col + 1}")
            step += 1
            print_board(board, n)

    return False


# User Input
print("=== N-Queens Problem using Backtracking ===")
n = int(input("Enter number of Queens (N): "))

if n <= 0:
    print("N must be a positive integer.")
    exit()

if n == 2 or n == 3:
    print(f"No solution exists for N = {n}.")
    exit()

# Initialize N x N board with 0
board = [[0 for _ in range(n)] for _ in range(n)]

print(f"\nEnter position for the 1st Queen (1 to {n}):")
first_row = int(input(f"  Enter row (1 to {n}): ")) - 1
first_col = int(input(f"  Enter column (1 to {n}): ")) - 1

# Validate user input position
if not (0 <= first_row < n and 0 <= first_col < n):
    print("Invalid row or column entered.")
    exit()

# Place the first queen
board[first_row][first_col] = 1
print(f"\nInitial State: 1st Queen placed at Row {first_row + 1}, Column {first_col + 1}:")
print_board(board, n)

# Remaining rows to place queens
remaining_rows = [r for r in range(n) if r != first_row]

# Solve using backtracking
if solve_nqueens(board, 0, remaining_rows, n):
    print("\n=== FINAL N-QUEENS MATRIX ===")
    print_board(board, n)
else:
    print(f"\nNo solution exists with the first Queen placed at ({first_row + 1}, {first_col + 1}).")