"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root
    @param k: an integer
    @return: the value of the nearest leaf node to target k in the tree
    """
    def findClosestLeaf(self, root, k):
        # Write your code here
        
        self.startNode = None
        
        graph = {}
        
        visited = {}
        
        self.buildGraph(graph,root,None,k)
        
        q = [self.startNode]
        
        
        while q != []:
            
            for _ in range(len(q)):
                
                front = q.pop(0)
                
                if not front.left and not front.right:
                    return front.val
                    
                visited[front] = 1
                
                for c in graph[front]:
                    if c in visited:
                        continue
                    q.append(c)
        return 0
        
        
        
    def buildGraph(self,graph,node,parent,k):
        if not node:
            return
        if node.val == k:
            self.startNode = node
        if parent:
            graph[parent] = graph.get(parent,[]) + [node]
            graph[node] = graph.get(node,[]) + [parent]
            
        self.buildGraph(graph,node.left,node,k)
        self.buildGraph(graph,node.right,node,k)
