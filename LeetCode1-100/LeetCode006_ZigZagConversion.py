# String
class Solution1(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        curRow = 0
        rowChange = 1
        res = [""] * numRows
        
        for char in s:
            res[curRow] += char # adds char to the correct row
            if numRows > 1:
                curRow += rowChange # curRow goes downward or goes upwards (zig zagging)
                if curRow == 0 or curRow == numRows -1: # if you reach the first row or the last row
                    rowChange *= -1 # switch directions
        
        return "".join(res)