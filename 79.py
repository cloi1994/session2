class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = [ [ 0 for _ in range(len(board[0]))]  for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(i,j,0,board,word,visited):
                    return True
                
        return False
    
    def dfs(self,i,j,index,board,word,visited):
        
        if index == len(word):
            return True
        
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[index] or visited[i][j]:
            return False
        
        visited[i][j] = True
        exist = self.dfs(i-1,j,index+1,board,word,visited) or self.dfs(i,j-1,index+1,board,word,visited) or self.dfs(i+1,j,index+1,board,word,visited) or self.dfs(i,j+1,index+1,board,word,visited)
        visited[i][j] = False
        return exist
        
