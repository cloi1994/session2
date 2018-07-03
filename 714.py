class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        sold = 0 
        hold = -prices[0]
       
        for p in prices:
            tmp = sold;
            sold = max(sold, hold + p - fee)
            hold = max(hold, t - p)
        
        return sold
            
        
