# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursion
import sys

class Solution1(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return self.helper(root)
    
    def helper(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        if root == None:
            return sys.maxsize
        
        if root.left == None and root.right == None:
            return 1
        
        leftDepth = self.helper(root.left)
        rightDepth = self.helper(root.right)
        
        return min(leftDepth, rightDepth) + 1


# Recursion
class Solution2(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        if root.left == None and root.right == None:
            return 1
        
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        
        if leftDepth == 0:
            return rightDepth + 1
        elif rightDepth == 0:
            return leftDepth + 1
        elif leftDepth < rightDepth:
            return leftDepth + 1
        else:
            return rightDepth + 1