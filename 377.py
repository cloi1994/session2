class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        dp = [1] + [-1] * target
        
        self.dfs(nums,target,dp)
        
        return dp[target]
        
    def dfs(self,nums,target,dp):
        
        if target < 0:
            return 0
        
        if dp[target] != -1:
            return dp[target]
        
        
        summ = 0
        for i in range(len(nums)):
            summ += self.dfs(nums,target-nums[i],dp)
        
        dp[target] = summ
        
        return summ
