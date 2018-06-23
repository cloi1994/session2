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
            
            
        count = 0
        minLen = len(s) + 1
        startIndex = 0
        res = ""
        
        for j in range(len(s)):
            
            if s[j] in tmap:
                
                if tmap[s[j]] >= 1:
                    count += 1
                    
                tmap[s[j]] -= 1
                
                while len(t) == count:
                    
                    if j - startIndex + 1 < minLen:
                        minLen = j - startIndex + 1
                        res = s[startIndex:j+1]
                        
                        
                    if s[startIndex] in tmap:
                        
                        if tmap[s[startIndex]] >= 0:
                            count -= 1
                        
                        tmap[s[startIndex]] += 1
                        

                            
                    startIndex += 1
                        
                        
                
            
            
            
        return res
            
        
        
