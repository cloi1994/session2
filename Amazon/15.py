class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        
        res = []
        
        for i in range(len(nums)-2):
            
            j = i + 1
            k = len(nums) - 1
            
            if i != 0 and nums[i-1] == nums[i]:
                continue
            
            while j < k:
                
                summ = nums[i] + nums[j] + nums[k]
                
                if summ == 0:
                    
                    res.append([nums[i],nums[j],nums[k]])
                    
                    while j + 1 < k and nums[j] == nums[j+1]:
                        j += 1
                        
                    while j < k - 1 and nums[k] == nums[k-1]:
                        k -= 1
                        
                    j += 1
                    k -= 1
                elif summ < 0:
                    j += 1  
                else:
                    k -= 1
                    
        return res
                
                
            
            
        
