class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        hm = {}
        left = 0
        
        
        for i in range(len(paragraph)+1):
            
            if i == len(paragraph) or paragraph[i] == ' ':
                
                s = paragraph[left:i].lower()
                
                if s == '':
                    left = i + 1
                    continue
                
                if not s[-1].isalpha():
                    s = s[:len(s)-1]
                
                hm[s] = hm.get(s,0) + 1
                
                left = i + 1
        res = []
            
        for h in hm:
            res.append([-hm[h],h])
            
        res.sort()
        
        for r in res:
            if r[1] in banned:
                continue
            return r[1]
        
        return ""
            
            
            
            
        
