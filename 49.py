class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        hm = {}
        res = []
        for s in strs:
            key = ''.join(sorted(s))
            hm[key] = hm.get(key,[]) + [s]
            
        for v in hm.values():
            res.append(v)
        
        return res
        
