# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        
        queue = [root]
        
        parent = {root: None}
    
        while p not in parent or q not in parent:
            node = queue.pop(0)
            
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)
                
        ancestor = []

        while p != None:
            ancestor.append(p)
            p = parent.get(p,None)
        
        while q not in ancestor:
            q = parent.get(q,None)
            
        return q
