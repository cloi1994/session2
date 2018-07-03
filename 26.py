class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        before = 1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                nums[before] = nums[i]
                before += 1
                
        return before
        
