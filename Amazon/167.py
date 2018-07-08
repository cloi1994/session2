class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            n = target - nums[i]
            
            low = i + 1
            high = len(nums) - 1
            
            while low <= high:
                mid = low + (high - low) // 2
                
                if nums[mid] == n:
                    return [i+1,mid+1]
                if nums[mid] > n:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1
