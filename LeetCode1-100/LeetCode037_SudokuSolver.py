# Backtracking (prefer Solution2)
# This is slower because it loops through even if the space is not empty
class Solution1(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solvePuzzle()
        
    def solvePuzzle(self):
        row, col = self.findEmptyCell()
        nums = ["1","2","3","4","5","6","7","8","9"]
        
        if row == -1 and col == -1:
            return True
        
        for num in nums:
            if self.isSafe(row, col, num):
                self.board[row][col] = num
                if self.solvePuzzle():
                    return True
                self.board[row][col] = "."
        return False
        
    def isSafe(self, row, col, num):
        # check if it is safe to put num in board[row, col]
        # find index of top left corner of each 3 x 3 square
        boxRow = row - row % 3
        boxCol = col - col % 3
        return self.checkRow(row, num) and self.checkCol(col, num) and self.checkSquare(boxRow, boxCol, num)
        
    def findEmptyCell(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.board[i][j] == ".":
                    return i, j
                
        return -1, -1
    
    def checkRow(self, row, num):
        # checks if you can put num in currrent row
        for col in range(0, 9):
            if self.board[row][col] == num:
                return False
        return True
    
    def checkCol(self, col, num):
        # checks if you can put num in currrent column
        for row in range(0, 9):
            if self.board[row][col] == num:
                return False
        return True
       
    def checkSquare(self, row, col, num):
        # checks if you can put num in currrent 3 x 3 square
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if self.board[r][c] == num:
                    return False
        return True

# Backtracking (preferred solution)
# This is faster because it only loops if the spot is empty
class Solution2(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solvePuzzle(0, 0)
        
    def solvePuzzle(self, row, col):    
        if row == 9: # if finished
            return True
        
        if col >= 9: # if should move on to next row
            return self.solvePuzzle(row + 1, 0)
        
        if self.board[row][col] == ".": # if board[row][col] is empty
            for num in range(1, 10): # num = the number to try into the empty spot
                if self.isSafe(row, col, str(num)): # if it is safe to place at board[row][col]
                    self.board[row][col] = str(num)
                    if self.solvePuzzle(row, col + 1):
                        return True
            self.board[row][col] = "."
        else:
            return self.solvePuzzle(row, col + 1) # move onto next column
        
        return False

    def isSafe(self, row, col, num):
        # check if it is safe to put num in board[row, col]
        # find index of top left corner of each 3 x 3 square
        boxRow = row - row % 3
        boxCol = col - col % 3
        return self.checkRow(row, num) and self.checkCol(col, num) and self.checkSquare(boxRow, boxCol, num)
        
    def findEmptyCell(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.board[i][j] == ".":
                    return i, j
                
        return -1, -1
    
    def checkRow(self, row, num):
        # checks if you can put num in currrent row
        for col in range(0, 9):
            if self.board[row][col] == num:
                return False
        return True
    
    def checkCol(self, col, num):
        # checks if you can put num in currrent column
        for row in range(0, 9):
            if self.board[row][col] == num:
                return False
        return True
       
    def checkSquare(self, row, col, num):
        # checks if you can put num in currrent 3 x 3 square
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if self.board[r][c] == num:
                    return False
        return True