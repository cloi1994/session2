"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""



class Solution(object):
    def checkEqualTree(self, root):
        seen = []
        
        def dfs(root):
            if not root:
                return 0
            seen.append(dfs(root.left) + dfs(root.right) + root.val)
            
            return seen[-1]
        
        
        dfs(root)
        
        total = seen[-1]
        
        seen.pop()
        
        return total / 2.0 in seen
