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
        
        if not root:
            return root
        
        hm = {root:None}
        
        que = [root]
        
        while p not in hm or q not in hm:
            node = que.pop(0)
            
            if node.left:
                que.append(node.left)
                hm[node.left] = node
            if node.right:
                que.append(node.right)
                hm[node.right] = node
                
        sset = set()
        
        
        while p != None:
            sset.add(p)
            p = hm.get(p,None)
            
        while q not in sset:
            q = hm.get(q,None)
            
        return q
            
                
        
            
            
            
        
