# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    def levelOrder(self, root):
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
            levelRes = []
            for _ in range(0, queue.size()):
                node = queue.dequeue()
                levelRes.append(node.val)
                
                if node.left != None:
                    queue.enqueue(node.left)
                if node.right != None:
                    queue.enqueue(node.right)
                
            res.append(levelRes)
            
        return res