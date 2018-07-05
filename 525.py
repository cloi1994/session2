class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        summ = 0
        
        
        m = {0:-1}
        
        
        for i in range(len(nums)):
            if nums[i] == 1:
                summ += 1
            else:
                summ -= 1 
            
            if summ in m:
                res = max(res, i - m[summ])
            else:
                m[summ] = i
            
        return res
        
