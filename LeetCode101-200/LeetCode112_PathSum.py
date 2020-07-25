# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        
        sum -= root.val
        
        if root.right == None and root.left == None: # if they both ended, return whether sum == 0
            return sum == 0
        
        return self.hasPathSum(root.right, sum) or self.hasPathSum(root.left, sum)