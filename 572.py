# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        
        
        return self.dfs(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
        
    def dfs(self,s,t):
        
        if not s and not t:
            return True
        
        if not s or not t:
            return False
        
        if t.val != s.val:
            return False 
        
        return self.dfs(s.left,t.left) and self.dfs(s.right,t.right)
