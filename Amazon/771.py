class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        hm = {}
        
        cnt = 0
        
        for j in J:
            hm[j] = hm.get(j,0) + 1
            
        for s in S:
            if s in hm:
                cnt += 1
                
        return cnt
