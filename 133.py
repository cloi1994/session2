# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        
        
        self.dic = {}
        return self.dfs(node)
        
    
    def dfs(self,node):
        
        if not node:
            return None
        
        if node in self.dic:
            return self.dic[node]
        
        newNode = UndirectedGraphNode(node.label)
        self.dic[node] = newNode
        
        for n in node.neighbors:
            newNode.neighbors.append(self.dfs(n))
            
        return newNode

        
        
