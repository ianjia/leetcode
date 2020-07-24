# Binary search (modified)
class Solution1(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        rows, columns = len(matrix), len(matrix[0])
        start, end = 0, rows * columns - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            midNum = matrix[mid // columns][mid % columns]
            if target == midNum:
                return True
            elif target < midNum:
                end = mid
            else:
                start = mid
                    
        if matrix[start//columns][start%columns] == target or matrix[end//columns][end%columns] == target:
            return True
        return False

# Binary search
class Solution2(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        
        rows, columns = len(matrix), len(matrix[0])
        start, end = 0, rows * columns - 1
        
        while start <= end:
            mid = (start + end) // 2
            midNum = matrix[mid // columns][mid % columns]
            if target == midNum:
                return True
            else:
                if target < midNum:
                    end = mid - 1
                else:
                    start = mid + 1
                    
        return False