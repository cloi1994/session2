class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """
    def numberofDistinctIslands(self, grid):
        # write your code here
        
        #visited = [[ 0 for _ in range(grid[0])] for _ in range(grid)]
        
        res = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                tmp = self.dfs(grid,i,j,i,j,res)
                if tmp == '':
                    continue
                if tmp not in res:
                    res.append(tmp)
                    
        return len(res)
                
                
    def dfs(self,grid,i,j,oi,oj,res):
        
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return ''
        
        grid[i][j] = 0
        

        child = self.dfs(grid,i+1,j,oi,oj,res) + self.dfs(grid,i,j+1,oi,oj,res) + self.dfs(grid,i-1,j,oi,oj,res) + self.dfs(grid,i,j-1,oi,oj,res)
        
        return str(i-oi) + "_" +  str(j-oj) + child
        
        
        
        
        
        
        
                
    
