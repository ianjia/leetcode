# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

# Queue
class Solution1(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root == None:
            return res
        
        queue = Queue()
        queue.enqueue(root)
        
        while queue.isEmpty() == False:
            levelSize = queue.size()
            levelRes = []
            for _ in range(0, levelSize):
                node = queue.dequeue()
                levelRes.append(node.val)
                if node.left != None:
                    queue.enqueue(node.left)
                if node.right != None:
                    queue.enqueue(node.right)
                
            res.append(levelRes)
            
        return res[::-1]