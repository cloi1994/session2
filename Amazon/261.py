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
        
        print graph
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

            res = self.dfs(graph,visited,c,node)
                
            print 'Node' + str(c) + '...' + str(res)
                
            if not res:
                return False
            
        return True
            
            
        
