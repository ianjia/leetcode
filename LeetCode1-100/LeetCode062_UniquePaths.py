# Dynamic Programming
class Solution1(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        matrix = [[0 for col in range(n)] for row in range(m)] 
        
        # the two for loops below sets all edges to 1
        for i in range(0, m):
            matrix[i][0] = 1
            
        for i in range(0, n):
            matrix[0][i] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1] # matrix[i][j] depends on the paths to the grid above and to the left of matrix[i][j] 
        
        return matrix[m-1][n-1] # return bottom right corner (finish)

# Math
class Solution2(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # These two lines below are needed because the robot is walking on a grid and not on a line
        m -= 1
        n -= 1
        
        return self.factorial(m + n) // (self.factorial(n) * self.factorial(m))
        
    def factorial(self, num):
        if num == 1:
            return 1
        
        return num * self.factorial(num - 1)