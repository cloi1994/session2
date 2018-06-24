# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return self.dfs(root,float('-inf'),float('inf'))
        
        
    def dfs(self,root,minLeft,maxRight):
        
        if not root:
            return True
        
        if root.val <= minLeft or root.val >= maxRight:
            return False
        
        return self.dfs(root.left,minLeft,root.val) and self.dfs(root.right,root.val,maxRight)
        
        
        
        

        
        
