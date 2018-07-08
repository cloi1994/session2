class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        self.left = 0
        self.maxLen = 0
        
        for i in range(len(s)):
            self.expand(i,i,s)
            self.expand(i,i+1,s)
            
        return s[self.left:self.left+self.maxLen]
            
    def expand(self,left,right,s):
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        left += 1  #above exceeded
        right -= 1
        
        
        if self.maxLen < right - left + 1:
            self.maxLen = right - left + 1
            self.left = left
        
        
