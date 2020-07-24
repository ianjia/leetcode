# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursion
class Solution1(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        
        return max(leftDepth, rightDepth) + 1

# Recursion
class Solution2(object):
    def maxDepth(self, root):
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
            return 0
        
        if root.left == None and root.right == None:
            return 1
        
        leftDepth = self.helper(root.left)
        rightDepth = self.helper(root.right)
        
        return max(leftDepth, rightDepth) + 1