class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hm = {}
        
        for c in s:
            hm[c] = hm.get(c,0) + 1
            
        for i in range(len(s)):
            if hm[s[i]] == 1:
                return i
        return -1
