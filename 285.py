"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        
        
        self.found = False
        self.ans = None
        self.dfs(root,p)
        
        return self.ans
        
    def dfs(self,root,p):
        
        if not root:
            return
        
        self.dfs(root.left,p)
        
        print root.val
        
        if self.found:
            self.ans = root
            self.found = False
            return 
        
        if root.val == p.val:
            self.found = True
        
        self.dfs(root.right,p)
        
        
