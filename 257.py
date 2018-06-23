# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
            
        tmp = ""
        res = []
        self.dfs(root,tmp,res)
        
        return res

    def dfs(self,root,tmp,res):
        
        if not root:
            return
        
        
        tmp += str(root.val)
        if not root.left and not root.right:
            res.append(tmp)
          
        tmp += "->"
        
        self.dfs(root.left,tmp,res)
        self.dfs(root.right,tmp,res)
        
        
