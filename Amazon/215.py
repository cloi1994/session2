from heapq import heappush, heappop

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        hq = []
        
        for n in nums:
            heappush(hq,n) 
            
            if len(hq) > k:
                heappop(hq)
                
        return hq[0]
                
            
        
