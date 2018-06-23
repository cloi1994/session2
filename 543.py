# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.diameter = 0
        self.lp(root)
        
        return self.diameter
    def lp(self,root):
        
        if not root:
            return 0
        
        left = self.lp(root.left)
        right = self.lp(root.right)
        
        self.diameter = max(self.diameter,left+right)
        
        return 1 + max(left,right)
