class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        hm = {}
        
        for ele in s:
            hm[ele] = hm.get(ele,0) + 1
            
            
        tmp = []
        for key in hm:
            tmp.append([key,hm[key]])
            
        tmp.sort(key= lambda x:-x[1])
        
        res = ""
        
        for t in tmp:
            res += t[0] * t[1]
            
        return res
        
