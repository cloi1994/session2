class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.res = 0
        self.dfs(0,nums,S)
        
        return self.res
        
        
    def dfs(self,level,nums,S):
        
        
        
        if level == len(nums):
            if S == 0:
                self.res += 1
            return
            
            
        self.dfs(level+1,nums,S-nums[level])
        self.dfs(level+1,nums,S+nums[level])
        
        
        
        
