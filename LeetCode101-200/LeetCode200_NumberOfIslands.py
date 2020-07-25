class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Queue(object):
    def __init__(self):
        self._items = []

    def isEmpty(self):
        return self._items == []

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)
    
    def pop(self):
        self._items.pop()

# BFS
class Solution1(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        
        rows = len(grid)
        columns = len(grid[0])
        numOfIslands = 0
        
        for i in range(0, rows):
            for j in range(0, columns):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    self.markThroughBFS(grid, i, j)
                    numOfIslands += 1
                    
        return numOfIslands
    
    def markThroughBFS(self, grid, row, column):
            rowChange = [-1, 0, 1, 0]
            columnChange = [0, 1, 0, -1]
            
            position = Coordinate(row, column)
            queue = Queue()
            queue.enqueue(position)
            while queue.isEmpty() == False:
                curPos = queue.dequeue()
                for i in range(0, 4):
                    newPos = Coordinate(curPos.x + rowChange[i], curPos.y + columnChange[i])
                    if self.isPosInBounds(grid, newPos) and grid[newPos.x][newPos.y] == "1":
                        grid[newPos.x][newPos.y] = "0"
                        queue.enqueue(newPos)                 
                        
    def isPosInBounds(self, grid, pos):
        rows = len(grid)
        columns = len(grid[0])
        if pos.x >= 0 and pos.x < rows and pos.y >= 0 and pos.y < columns:
            return True
        return False

# DFS
class Solution2(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        
        rows = len(grid)
        columns = len(grid[0])
        numOfIslands = 0
        
        for i in range(0, rows):
            for j in range(0, columns):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    self.markThroughDFS(grid, i, j)
                    numOfIslands += 1
                    
        return numOfIslands
    
    def markThroughDFS(self, grid, row, column):
            rowChange = [-1, 0, 1, 0]
            columnChange = [0, 1, 0, -1]
            
            curPos = Coordinate(row, column)
            for i in range(0, 4):
                newPos = Coordinate(curPos.x + rowChange[i], curPos.y + columnChange[i])
                if self.isPosInBounds(grid, newPos) and grid[newPos.x][newPos.y] == "1":
                    grid[newPos.x][newPos.y] = "0"
                    self.markThroughDFS(grid, newPos.x, newPos.y)
                                            
                        
    def isPosInBounds(self, grid, pos):
        rows = len(grid)
        columns = len(grid[0])
        if pos.x >= 0 and pos.x < rows and pos.y >= 0 and pos.y < columns:
            return True
        return False