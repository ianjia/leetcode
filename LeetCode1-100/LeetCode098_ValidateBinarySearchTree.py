# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Inorder traversal
class Solution1(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        inorder = self.inorderTraversal(root)
        
        for i in range(0, len(inorder) - 1):
            if inorder[i] >= inorder[i + 1]: # check if they don't meet the BST requirements
                return False
            
        return True
        
    def inorderTraversal(self, root):
        res = []
        
        if root == None:
            return res
        
        leftRes = self.inorderTraversal(root.left)
        rightRes = self.inorderTraversal(root.right)
        res.extend(leftRes)
        res.append(root.val)
        res.extend(rightRes)
        
        return res

# Divide & Conquer Recursion
import sys

class Solution2(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isBST(root, -sys.maxsize, sys.maxsize)
        
    def isBST(self, root, curSmall, curLarge):
        if root == None:
            return True
        
        if root.val <= curSmall or root.val >= curLarge:
            return False
        
        if self.isBST(root.right, root.val, curLarge) == False:
            return False
        if self.isBST(root.left, curSmall, root.val) == False:
            return False
        
        return True