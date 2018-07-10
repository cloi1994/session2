class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        
        if not board:
            return board
        
        x,y = click
        
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        
        
        
        self.dfs(board,x,y)
        
        return board
        
    def dfs(self,board,i,j):
        
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return 
        
        if board[i][j] != 'E':
            return 
        

        dirs = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]
        
        val = 0
        
        for d in dirs:
            newX = i + d[0]
            newY = j + d[1]
            
            if newX < 0 or newY < 0 or newX >= len(board) or newY >= len(board[0]):
                continue
            if board[newX][newY] == 'M':
                val += 1
        
        if val == 0:
            board[i][j] = 'B'
            for d in dirs:
                newX = i + d[0]
                newY = j + d[1]

                self.dfs(board,newX,newY)
            
        else:
            board[i][j] = str(val)
