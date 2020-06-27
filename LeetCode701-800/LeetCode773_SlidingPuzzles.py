# BFS
import copy

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

class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        rows = len(board)
        columns = len(board[0])
        target = "123450"
        visited = set()
        moves = 0
        queue = Queue()
        rowChange = [-1, 0, 1, 0]
        columnChange = [0, 1, 0, -1]
        
        strOfBoard = self.matrixToStr(board, rows, columns)
        if strOfBoard == target:
            return 0
        
        queue.enqueue(strOfBoard)
        visited.add(strOfBoard)
        while queue.isEmpty() == False:
            moves += 1
            for i in range(0, queue.size()):
                curNode = self.strToMatrix(queue.dequeue(), rows, columns)
                # finds the position of the empty slot (in this case is 0)
                for i in range(0, rows):
                    for j in range(0, columns):
                        if curNode[i][j] == 0:
                            position = Coordinate(i, j)
                            break
                
                for i in range(0, 4):
                    newPos = Coordinate(position.x + rowChange[i], position.y + columnChange[i])
                    if self.isPosInBounds(curNode, newPos):
                        newNode = copy.deepcopy(curNode)
                        newNode[newPos.x][newPos.y], newNode[position.x][position.y] = newNode[position.x][position.y], newNode[newPos.x][newPos.y]
                        if self.matrixToStr(newNode, rows, columns) not in visited:
                            strOfNewNode = self.matrixToStr(newNode, rows, columns)
                            if strOfNewNode == target:
                                return moves
                            queue.enqueue(strOfNewNode)
                            visited.add(strOfNewNode)
                    
        return -1
                
    def isPosInBounds(self, matrix, pos):
        rows = len(matrix)
        columns = len(matrix[0])
        if pos.x >= 0 and pos.x < rows and pos.y >= 0 and pos.y < columns:
            return True
        return False
    
    def matrixToStr(self, matrix, rows, columns):
        strOfMatrix = ""
        
        for i in range(0, rows):
            for j in range(0, columns):
                strOfMatrix += str(matrix[i][j])
                
        return strOfMatrix
    
    def strToMatrix(self, strOfMatrix, rows, columns):
        matrix = []
        
        matrix.append(list(strOfMatrix[:columns]))
        matrix.append(list(strOfMatrix[columns:]))
        
        for i in range(0, rows):
            for j in range(0, columns):
                matrix[i][j] = int(matrix[i][j])
        
        return matrix