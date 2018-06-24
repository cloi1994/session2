from heapq import heappush, heappop

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        q = []
        
        for n in nums:
            heappush(q,n)
            if len(q) > k:
                heappop(q)
                
        return q[0]
 
