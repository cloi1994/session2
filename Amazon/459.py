class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        
        for i in range(n/2,0,-1):
            if n % i == 0:                                
                c = n/ i
                
                tmp = s[0:i] * c
                
                if tmp == s:
                    return True
                
        return False
