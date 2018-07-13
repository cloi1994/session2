class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        
        hm = {}
        
        for k in range(len(S)):
            hm[S[k]] = k
        
        start = 0 
        end = 0
        res = []

        for i in range(len(S)):
            end = max(end,hm[S[i]])
            
            if i == end:
                res.append(end-start+1)
                start = i + 1
                
        return res
