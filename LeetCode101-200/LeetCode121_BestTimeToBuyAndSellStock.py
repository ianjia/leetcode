# One Pass
import sys

class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        lowestPrice = sys.maxsize
        
        for i in range(0, len(prices)):
            if prices[i] < lowestPrice:
                lowestPrice = prices[i]
            elif prices[i] - lowestPrice > maxProfit:
                maxProfit = prices[i] - lowestPrice
                
        return maxProfit