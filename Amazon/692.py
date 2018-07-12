from heapq import heappush,heappop

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        hm = {}
        
        for w in words:
            hm[w] = hm.get(w,0) + 1
            
        hq = []
        res = []
           
        for key in hm.keys():
            heappush(hq,(-hm[key],key))
            
        for i in range(k):
            res.append(heappop(hq)[1])
            
        return res
            
        
            
        
