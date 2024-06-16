def validate_sudoku(board):
    for row in board:
        row_vals = set(row)
        if len(row_vals) != 9 or 0 in row_vals:
            return False

    for j in range(len(board[0])):
        col_vals = set()
        for i in range(len(board)):
            col_vals.add(board[i][j])

        if len(col_vals) != 9 or 0 in col_vals:
            return False

    for i in range(len(board)):
        block_vals = set()
        for j in range(len(board[i])):
            row = i * 3 % 9 + j % 3
            col = j // 3
            print(row, col)
            block_vals.add(board[row][col])

        if len(block_vals) != 9 or 0 in block_vals:
            return False

    return True
