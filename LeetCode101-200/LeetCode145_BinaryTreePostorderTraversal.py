# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        
        if root == None:
            return res
        
        leftRes = self.postorderTraversal(root.left)
        rightRes = self.postorderTraversal(root.right)
        res.extend(leftRes)
        res.extend(rightRes)
        res.append(root.val)
        
        return res