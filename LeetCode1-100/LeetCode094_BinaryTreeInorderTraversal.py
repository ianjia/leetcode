# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Divide and Conquer (not follow up)
class Solution1(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        
        if root == None:
            return res
        
        leftRes = self.inorderTraversal(root.left)
        rightRes = self.inorderTraversal(root.right)
        res.extend(leftRes)
        res.append(root.val)
        res.extend(rightRes)
        
        return res