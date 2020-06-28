class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if len(matrix) == 0: 
            return res
        
        rows = len(matrix)
        columns = len(matrix[0])
        seen = [[False] * columns for k in matrix]
        rowChange = [0, 1, 0, -1]
        columnChange = [1, 0, -1, 0]
        i = 0
        j = 0
        direction = 0
        for k in range(rows * columns):
            res.append(matrix[i][j])
            seen[i][j] = True
            rowPos = i + rowChange[direction]
            columnPos = j + columnChange[direction]
            if 0 <= rowPos < rows and 0 <= columnPos < columns and seen[rowPos][columnPos] == False: # in bound and not visited, does not turn
                i = rowPos
                j = columnPos
            else: # turns
                direction = (direction + 1) % 4
                i = i + rowChange[direction]
                j = j + columnChange[direction]
                
        return res