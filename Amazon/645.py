class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        a = []
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        missing, repeating = None, None
        for i in range(1,len(nums)+1):
            if i not in d:
                missing = i
            elif d[i] == 2:
                repeating = i
        return [repeating, missing]
