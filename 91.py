class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s or len(s) == 0:
            return 0
        
        length = len(s)

        dp = [0] * (length+1)
        
        dp[0] = 1
        
        if int(s[0]) != 0:
            dp[1] = 1
        
        for i in range(2,length+1):
            
            first = s[i-1:i]
            second = s[i-2:i]
            
            if 1 <= int(first) <= 9:
                dp[i] += dp[i-1]
            
            if 26 >= int(second) >= 10:
                dp[i] += dp[i-2]

        return dp[length]
