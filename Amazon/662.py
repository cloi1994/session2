# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        q = [[root,1]]
        
        res = 0

        
        while q:
            
            left = q[0][1]
            right = q[0][1]
            
            size = len(q)
            
            for i in range(size):
                
                node, right = q.pop(0)
                
                if node.left:
                    q.append([node.left,right*2])
                if node.right:
                    q.append([node.right,right*2+1])
                    
            res = max(res,right-left + 1)
            
        return res
                
                
                
                
            
            
        
