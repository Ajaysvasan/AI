N = 9  # Size of the Sudoku grid (9x9)

def printing(arr):
    """
    Prints the Sudoku grid in a formatted way.
    """
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()


def isSafe(grid, row, col, num):
    """
    Checks if it's safe to place a number in the given row and column.
    """
    # Check the row
    for x in range(9):
        if grid[row][x] == num:
            return False
    
    # Check the column
    for x in range(9):
        if grid[x][col] == num:
            return False
    
    # Check the 3x3 subgrid
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    
    return True


def solveSudoku(grid, row, col):
    """
    Solves the Sudoku puzzle using backtracking.
    """
    # If we've reached the end of the grid, return True
    if row == N - 1 and col == N:
        return True

    # Move to the next row if at the end of a column
    if col == N:
        row += 1
        col = 0

    # If the cell is already filled, move to the next cell
    if grid[row][col] > 0:
        return solveSudoku(grid, row, col + 1)

    # Try placing numbers 1 to 9 in the cell
    for num in range(1, N + 1):
        if isSafe(grid, row, col, num):
            grid[row][col] = num  # Place the number

            # Recursively attempt to solve the rest of the grid
            if solveSudoku(grid, row, col + 1):
                return True

            # Undo the move (backtracking)
            grid[row][col] = 0

    return False  # If no number can be placed, backtrack


# Initial Sudoku grid with some pre-filled values
grid = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]

# Solve the Sudoku puzzle and print the solution
if solveSudoku(grid, 0, 0):
    printing(grid)
else:
    print("No solution exists")
