class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []      
        
        dic = {'}':'{', ')':'(',']':'['}
        
        for sym in s:
            if sym == '{' or sym == '[' or  sym == '(':
                stack.append(sym)
            else:
                
                if stack == [] or stack[-1] != dic[sym]:
                    return False
                stack.pop()
                
        return len(stack) == 0
                
                
        
