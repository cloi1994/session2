"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        def cmpfuc(x,y):
            return x.start - y.start
            
        if not intervals:
            return True

        intervals.sort(cmp=cmpfuc)
        
        res = [intervals[0]]
        
        
    
        for i in range(1,len(intervals)):
            if intervals[i-1].end > intervals[i].start:
                return False
                
        return True

