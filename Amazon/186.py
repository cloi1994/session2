class Solution:
    """
    @param str: a string
    @return: return a string
    """
    def reverseWords(self, str):
        # write your code here
        
        newstr = list(str)
        
        i = 0
        
        for j in range(len(newstr)+1):
            
            if  j == len(newstr) or newstr[j] == ' ':
                self.reverse(i,j-1,newstr)
                i = j+1
                
        return ''.join(newstr[::-1])
                
    def reverse(self,start,end,newstr):
        
        while start < end:
            newstr[end] , newstr[start] = newstr[start], newstr[end]
            start += 1
            end -= 1
            

        
