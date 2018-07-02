class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        globalDir = []
        curDir = []
        
        path = path.split('/')
        
        
        for p in path:
            
            if p == '' or p == '.':
                continue 
            elif p == '..':
                if curDir != []:
                    curDir.pop()
            else:
                curDir.append(p)

        
        return  '/'+'/'.join(curDir)
                
            
        
        
