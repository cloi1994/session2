class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        summ = dic[s[-1]]
        
        for i in range(len(s)-2,-1,-1):
            if dic[s[i+1]] > dic[s[i]]:
                summ -= dic[s[i]]
            else:
                summ += dic[s[i]]
                
        return summ
        
        
        
        
