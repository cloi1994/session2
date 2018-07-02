class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        
        hm = {}
        
        for i in range(len(wall)):
            summ = 0
            for j in range(len(wall[i])-1):
                summ += wall[i][j]
                hm[summ] = hm.get(summ,0) + 1 
        print hm.values()     
        return len(wall) - max(hm.values()+[0])
                
        
        
