class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        hm = {}
        
        for c in s:
            hm[c] = hm.get(c,0) + 1
        
        for c in t:
            if c not in hm or hm[c] <= 0:
                return False
            hm[c] -= 1
        
        return True
            
