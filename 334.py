class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        num1 = None
        num2 = None
        
        
        for n in nums:
            
            if num1 != None and num2 != None and num2 < n:
                return True
            
            if num1 == None or n < num1:
                num1 = n
            elif num1 != None and num1 < n:
                num2 = n   

            
        return False
        
