class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Pre-compute empty cells to avoid scanning the entire board repeatedly
        empty_cells = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty_cells.append((i, j))
        
        # Pre-compute which values are already used in each row, column, and box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    digit = board[i][j]
                    rows[i].add(digit)
                    cols[j].add(digit)
                    box_idx = (i // 3) * 3 + j // 3
                    boxes[box_idx].add(digit)
        
        def is_valid(row, col, digit):
            box_idx = (row // 3) * 3 + col // 3
            return digit not in rows[row] and digit not in cols[col] and digit not in boxes[box_idx]
        
        def backtrack(cell_idx):
            if cell_idx == len(empty_cells):
                return True
            
            row, col = empty_cells[cell_idx]
            box_idx = (row // 3) * 3 + col // 3
            
            for digit in '123456789':
                if is_valid(row, col, digit):
                    # Place the digit
                    board[row][col] = digit
                    rows[row].add(digit)
                    cols[col].add(digit)
                    boxes[box_idx].add(digit)
                    
                    # Recursive call
                    if backtrack(cell_idx + 1):
                        return True
                    
                    # Backtrack
                    board[row][col] = '.'
                    rows[row].remove(digit)
                    cols[col].remove(digit)
                    boxes[box_idx].remove(digit)
            
            return False
        
        backtrack(0)




        # def Solve(board):
        #     for i in range(len(board)):
        #         for j in range(len(board[0])):
        #             if board[i][j] == '.':
        #                 for c in range(1, 10):
        #                     # Convert c to string before checking validity
        #                     c_str = str(c)
        #                     if isValid(board, i, j, c_str):
        #                         board[i][j] = c_str
        #                         if Solve(board):
        #                             return True
        #                         else:
        #                             board[i][j] = '.'
        #                 # If no valid digit was found, return False to backtrack
        #                 return False
        #     return True

        # def isValid(board, row, col, c):
        #     for i in range(9):
        #         # Check row
        #         if board[row][i] == c:
        #             return False
                
        #         # Check column
        #         if board[i][col] == c:
        #             return False
                
        #         # Check 3x3 box
        #         box_row = 3 * (row // 3) + i // 3
        #         box_col = 3 * (col // 3) + i % 3
        #         if board[box_row][box_col] == c:
        #             return False
            
        #     return True
            
        # Solve(board)


        # def Solve(board):
        #     for i in range(len(board)):
        #         for j in range(len(board[0])):
        #             if board[i][j] == '.':
        #                 for c in range(1,10):
        #                     c_str = str(c)
        #                     if isValid(board, i, j, c_str):
        #                         board[i][j] = c_str
        #                         if Solve(board) == True:
        #                             return True
        #                         else:
        #                             board[i][j] = '.'
        #                 return False
        #     return True

        # def isValid(board, row, col, c):
        #     for i in range(9):
        #         if board[i][col] == c:
        #             return False
                
        #         if board[row][i] == c:
        #             return False

        #         # box_row = 3 * (row // 3) + i // 3
        #         # box_col = 3 * (col // 3) + i % 3
        #         # if board[box_row][box_col] == c:
        #         #     return False
        #         if board[3*(row//3) + i//3][3*(col//3) + i % 3] == c:
        #             return False
            
        #     return True
        # Solve(board)
        