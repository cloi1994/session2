class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        v = [float('-inf'),float('-inf'),float('-inf')]
        
        
        for n in nums:
            if n not in v:
                print n
                print v
                if n > v[0]:
                    v[2] = v[1]
                    v[1] = v[0]
                    v[0] = n
                elif n > v[1]:
                    v[2] = v[1]
                    v[1] = n
                elif n > v[2]:
                    v[2] = n
                    
        if v[2] != float('-inf'):
            return v[2]
        else:
            return v[0]
                
                
