class Solution(object):
    def numberToWords(self, num):
        
        if num == 0:
            return "Zero"
        else:
            res = self.intToWords(num)
            print res
            return res[1:len(res)]
        
        
        
    def intToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        digits = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["Zero", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        if num >= pow(10,9):
            return self.intToWords(num/pow(10,9)) + " Billion" + self.intToWords(num%pow(10,9))
        elif num >= pow(10,6):
            return self.intToWords(num/pow(10,6)) + " Million" + self.intToWords(num%pow(10,6))
        elif num >= pow(10,3):
            return self.intToWords(num/pow(10,3)) + " Thousand" + self.intToWords(num%pow(10,3))
        elif num >= pow(10,2):
            return self.intToWords(num/pow(10,2)) + " Hundred" + self.intToWords(num%pow(10,2))
        elif num >= 20:
            return " " + tens[num/10] + self.intToWords(num%10)
        elif num >= 1:
            return " " + digits[num]
        else:
            return ""
        
        
        
