# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        
        if not root:
            return root
        
        q = [root]
        
        while q != []:
            
            prev = None
            
            for i in range(len(q)):
                node = q.pop(0)
                
                if i == 0:
                    prev = node
                else: 
                    prev.next = node
                    prev = prev.next
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                
        
                    
                
                
