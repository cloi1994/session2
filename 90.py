class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        res = []
        self.dfs(0,nums,[],res)
        
        return res
    
    def dfs(self,index,nums,tmp,res):
        
        res.append(tmp[:])
        
        for i in range(index,len(nums)):
            
            if i != index and nums[i-1] == nums[i]: 
                continue
            tmp.append(nums[i])
            self.dfs(i+1,nums,tmp,res)
            tmp.pop()
        
        
