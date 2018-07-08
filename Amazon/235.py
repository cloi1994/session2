# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if not root or not p or not q:
            return root
        
        if p.val > q.val:
            return self.dfs(root,q,p)
        
        return self.dfs(root,p,q)
        
    def dfs(self,root,p,q):
    
        if not root:
            return None
        
        if root.val <= q.val and root.val >= p.val:
            return root
        if root.val > q.val and root.val > p.val:
            return self.dfs(root.left,p,q)
        if root.val < q.val and root.val < p.val:
            return self.dfs(root.right,p,q)
