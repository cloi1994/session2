class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        left = 0
        mid = 0
        right = len(nums) - 1
        

        while left <= right:
            if nums[left] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1    
            elif nums[left] == 1:
                left += 1
            elif nums[left] == 2:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1         
            else:
                raise ('Wrong Input')
            
            
            
