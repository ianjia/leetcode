# Backtracking
class Solution1(object):
    def __init__(self):
        self.res = 0
    
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        
        colPos = []
        self.dfs(colPos, n)
        return self.res
    
    def dfs(self, colPos, n):
        if len(colPos) == n:
            self.res += 1
            return
        
        for i in range(0, n):
            if not self.isValid(colPos, i):
                continue
            colPos.append(i)
            self.dfs(colPos, n)
            colPos.pop()
            
    def isValid(self, colPos, column):
        row = len(colPos)
        for i in range(0, row):
            if colPos[i] == column: # same column with an existing row
                return False
            # Check diagonal
            if i + colPos[i] == row + column:
                return False
            if i - colPos[i] == row - column:
                return False
        return True

# Backtracking
class Solution2(object):
    def __init__(self):
        self.res = 0
    
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        
        row = [-1] * n
        self.dfs(row, 0)
        return self.res
    
    def dfs(self, row, index):
        if index == len(row):
            self.res += 1
            return
        
        for i in range(0, len(row)):
            row[index] = i
            if self.isValid(row, index):
                self.dfs(row, index + 1)
    
    def isValid(self, row, index):
        for i in range(0, index):
            if row[i] == row[index] or abs(row[index] - row[i]) == abs(index - i):
                return False
        return True