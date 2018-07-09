class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        tmap = {}
        
        
        for ele in t:
            tmap[ele] = tmap.get(ele,0) + 1
            
        i = 0
        count = 0
        minLen = len(s) + 1
        
        res = ""
        
        for j in range(len(s)):
            
                
            if s[j] in tmap:
                tmap[s[j]] -= 1
                if tmap[s[j]] >= 0:
                    count += 1
                # minimize
            while count == len(t):
                    
                if minLen > j-i+1:
                    minLen = j -i + 1
                    res = s[i:j+1]
                    
                if s[i] in tmap:
                    tmap[s[i]] += 1
                    if tmap[s[i]] > 0:
                        count -= 1
                    
                i += 1    
            
            
        return res
