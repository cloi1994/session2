class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s or len(s) == 0:
            return 0
        
        self.res = 0
        
        for i in range(len(s)):
            self.extend(i,i+1,s)
            self.extend(i,i,s)
            
        return self.res
            
    def extend(self,left,right,s):
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            self.res += 1
            left -= 1
            right += 1
        
