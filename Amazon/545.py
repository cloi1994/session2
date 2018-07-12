"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode
    @return: a list of integer
    """
    def boundaryOfBinaryTree(self, root):
        # write your code here
        
        if not root:
            return []
        
        res = []
        
        if root.left or root.right:
            res.append(root.val)
            
        self.left(root.left,res)
        self.leaves(root,res)
        self.right(root.right,res)
        
        return res
        
    def left(self,root,res):
        if not root:
            return
        if not root.left and not root.right:
            return
        
        res.append(root.val)
        
        if not root.left:
            self.left(root.right,res)
    
        self.left(root.left,res)
        
        
    def leaves(self,root,res):
        if not root:
            return
        if not root.left and not root.right:
            res.append(root.val)
            
        self.leaves(root.left,res)
        self.leaves(root.right,res)
        
    
    def right(self,root,res):
        if not root:
            return
        if not root.left and not root.right:
            return
        
        if not root.right:
            self.right(root.left,res)
    
        self.right(root.right,res)
        
        res.append(root.val)  #be careful
