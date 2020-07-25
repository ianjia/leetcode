# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Divide and Conquer
class Solution1(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        
        if root == None:
            return res
        
        leftRes = self.preorderTraversal(root.left)
        rightRes = self.preorderTraversal(root.right)
        res.append(root.val)
        res.extend(leftRes)
        res.extend(rightRes)
        
        return res