# Dynamic Programming - O(m x n) space
class Solution1(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """  
        if obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        matrix = [[0 for col in range(n)] for row in range(m)] 

        for i in range(0, m):
            if obstacleGrid[i][0] == 1:
                matrix[i][0] = 0
                break # break because you can't continue if there was a obstacle
            else:
                matrix[i][0] = 1
            
        for i in range(0, n):
            if obstacleGrid[0][i] == 1:
                matrix[0][i] = 0
                break # break because you can't continue if there was a obstacle
            else:
                matrix[0][i] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        
        return matrix[m-1][n-1]

# Dynamic Programming - O(1) space
class Solution2(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """  
        if obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        obstacleGrid[0][0] = 1
        
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                obstacleGrid[i][0] = 0
            else:
                obstacleGrid[i][0] = obstacleGrid[i-1][0]     
            
        for i in range(1, n):
            if obstacleGrid[0][i] == 1:
                obstacleGrid[0][i] = 0
            else:
                obstacleGrid[0][i] = obstacleGrid[0][i-1]
            
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        
        return obstacleGrid[m-1][n-1]