# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        def cmpfuc(x,y):
            
            return x.start - y.start
            
            
        
        
        if not intervals:
            return []

        intervals.sort(cmp=cmpfuc)
        
        res = [intervals[0]]
    
        
        for i in range(1,len(intervals)):
            
            if intervals[i].start > res[-1].end:
                res.append(intervals[i])
            else:
                res[-1].end = max(res[-1].end,intervals[i].end)
            
        
        return res
        
