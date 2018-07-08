class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        
        aset = set()
        maxlen = 0  
        i = 0
        
        for j in range(len(s)):
            
            while s[j] in aset:
                aset.remove(s[i])
                i += 1
            
            maxlen = max(maxlen,j-i+1)
            aset.add(s[j])
            
        return maxlen
        
                
            
            
