class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        cnt = 1
        
        res = 1
        
        for i in range(1,len(nums)):
            
            if nums[i-1] < nums[i]:
                cnt += 1
                res = max(res,cnt) 
            else:
                cnt = 1
                
        return res
            
            
        
        
        
