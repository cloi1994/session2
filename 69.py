class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        i = 1
        j = x
        
        res = 0
        
        while i <= j:
            mid = i + (j-i) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                j = mid - 1
            else:
                i = mid + 1
                res = mid
                
        return res
