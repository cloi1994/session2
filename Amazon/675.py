class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        
        tree = []
        
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j] != 0:
                    tree.append([forest[i][j],i,j])
                    
        tree.sort(key=lambda x:x[0])
            
        startX = 0
        startY = 0
        
        q = []
        
        allstep = 0
        
        
        for t in tree:
            
            targetX, targetY = t[1],t[2]
            
            curStep = self.bfs(startX,startY,targetX,targetY,forest)    
            
            if curStep == -1:
                return -1
            
            allstep += curStep
            
            #forest[targetX][targetY] = 1
        
            startX = targetX
            startY = targetY
            
        return allstep
            
            
    def bfs(self,startX,startY,targetX,targetY,forest):
        
        if startX == targetX and startY == targetY:
            return 0
        
        q = [(startX,startY)]
        
        visited = [ [0 for _ in range(len(forest[0]))] for _ in range(len(forest))]
        
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        
        step = 0
        
        while q != []:
            
            
            
            for _ in range(len(q)):
                
                curX, curY = q.pop(0)
                
                if curX == targetX and curY == targetY:
                    return step
                
                for d in dirs:
                    
                    newX = curX + d[0]
                    newY = curY + d[1]
                    
                    if newX < 0 or newY < 0 or newX >= len(forest) or newY >= len(forest[0]) or forest[newX][newY] == 0 or visited[newX][newY]:
                        continue
                        
                    visited[newX][newY] = 1
                    q.append((newX,newY))
                    
            step += 1
            
        return -1
            
            
            
        
