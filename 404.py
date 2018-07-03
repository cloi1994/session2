# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        
        self.res = 0
        self.dfs(root)
        
        return self.res
        
    def dfs(self,root):
        
        if not root:
            return 0
        
        
        if root.left and not root.left.left and not root.left.right:
            self.res += root.left.val
            
        self.dfs(root.left)
        self.dfs(root.right)
            
            
        
