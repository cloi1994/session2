class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        
        graph = []
        
        for i in range(n):
            graph.append([])
            
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
           
        visited = {0:1}
        res = self.dfs(graph,visited,0,-1)
        
        print visited
        if res == False:
            return False
            
        if len(visited) != n:
            return False
            
        return res
    
    def dfs(self,graph,visited,node,parent):
        
        children = graph[node]
        
        for c in children:
            if c == parent:
                continue
            
            if c in visited:
                return False
            
            visited[c] = 1
            if not self.dfs(graph,visited,c,node):
                return False
            
        return True
 
# Solution 2

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        
        graph = []
        
        for i in range(n):
            graph.append([])
            
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
           
        visited = {}
        res = self.dfs(graph,visited,0,-1)
        
        print visited
        if res == False:
            return False
            
        if len(visited) != n:
            return False
            
        return res
    
    def dfs(self,graph,visited,node,parent):
        
        if node in visited:
            return False
            
        visited[node] = 1
        
        children = graph[node]
        
        for c in children:
            if c == parent:
                continue

            if not self.dfs(graph,visited,c,node):
                return False
            
        return True
            
            
        

        
