class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        #[1,1,3,4,5]
        
        if not nums or len(nums) == 0 or k < 0:
            return 0
        
        hm = {}
        
        cnt = 0
        
        for n in nums:
            hm[n] = hm.get(n,0) + 1
            
        for key in hm.keys():
            
            if k == 0:
                if hm[key] >= 2:
                    cnt += 1
            else:
                if key - k in hm:
                    cnt += 1
    
        
        return cnt
        
        
        
