class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        sMap = {}
        
        TMap = {}
        
        res = ""
        
        for ele in S:
            sMap[ele] = sMap.get(ele,0) + 1
        
        for ele in T:
            TMap[ele] = TMap.get(ele,0) + 1
         
        for ele in S:
            res += ele* TMap.get(ele,0)
                    
        for ele in T:
            if ele not in sMap:
                res += ele
                
        return res
            
        
