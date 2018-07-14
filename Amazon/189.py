class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        k %= len(nums)
        
        self.reverse(0,len(nums)-1,nums)
        self.reverse(0,k-1,nums)
        self.reverse(k,len(nums)-1,nums)
        
    def reverse(self,i,j,nums):
        
        while i < j:
            nums[i], nums[j] = nums[j] , nums[i]
            i += 1
            j -= 1
        
        
