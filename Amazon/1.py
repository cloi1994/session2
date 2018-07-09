class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dic = {}
        
        for i in range(len(nums)):
            
            rmd = target - nums[i]
            
            if rmd in dic:
                return [dic[rmd],i]
            else:
                dic[nums[i]] = i
                
        return None
