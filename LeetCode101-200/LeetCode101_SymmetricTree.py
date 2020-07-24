# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursion
class Solution1(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
    
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, treeOne, treeTwo):
        if treeOne == None and treeTwo == None: # if they both finished at the same time
            return True
        if treeOne == None or treeTwo == None: # if either one finished first
            return False
        if treeOne.val != treeTwo.val: # if their values do not equal each other
            return False
        if self.isMirror(treeOne.left, treeTwo.right) and self.isMirror(treeOne.right, treeTwo.left):
            return True
        
        return False