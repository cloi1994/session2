class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        dic = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        res = ''
        
        while n > 0:
            n -= 1
            res = dic[n%26] + res
            n /= 26
            
        return res
            
            
        
