class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if not digits:
            return []
        
        self.dict_num = { '1': '',    '2': 'abc', '3': 'def',
        '4': 'ghi', '5': 'jkl', '6': 'mno',
        '7': 'pqrs','8': 'tuv', '9': 'wxyz',
        '0': ' '}
        
        
        res = []
        
        self.dfs(digits,0,"",res)
        
        return res
        
    def dfs(self,digits,level,tmp,res):
        
        if len(tmp) == len(digits):
            res.append(tmp)
            return
        
        for ele in self.dict_num[digits[level]]:
            self.dfs(digits,level+1,tmp+ele,res)
