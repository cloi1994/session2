class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            
            
            if nums[mid] <= nums[right]:  # can't without == because mid only checks equal to target
                
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            elif nums[mid] > nums[right]:
                
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
        return -1
            
            
