from heapq import heappush, heappop

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        
        dic = {}
        
        pq = []
        
        res = 0
        
        for t in tasks:
            dic[t] = dic.get(t,0) + 1
            
            
        for v in dic.values():
            heappush(pq,-v)
        
            
        while pq != []:
            
            k = 0
            
            tmp = []
            
            for _ in range(n+1):
                if pq != []:
                    tmp.append(heappop(pq)+1)
                    k += 1
            
            for ele in tmp:
                if ele < 0:
                    heappush(pq, ele)

            if pq != []:
                res += n + 1
            else:
                res += k
                
        return res
                
            
            
            
        
            
        
