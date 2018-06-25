class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        # write your code here
        
        q = []
        
        dirs = [[-1,0], [0,-1],[1,0],[0,1]]
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append([i,j,0])
                    
                    
        while q != []:
            
            x,y,distance = q.pop(0)
            
            for d in dirs:
                
                newX = x + d[0]
                newY = y + d[1]
                
                self.addToQueue(newX,newY,q,rooms,distance+1)
                
    def addToQueue(self,x,y,q,rooms,distance):
        
        if x < 0 or y < 0 or x >= len(rooms) or y >= len(rooms[0]):
            return
            
        if rooms[x][y] != 2147483647:
            return
        
        rooms[x][y] = distance
        
        q.append([x,y,distance])
        
        
        
        
        
        
            
            
            
            
