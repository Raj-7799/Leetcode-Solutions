class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        maxReturn = [0 for i in range(len(prices))]
        
        high = 0
        for i in range(len(prices) -1, -1, -1):
            if prices[i] > high:
                high = prices[i]
                
            maxReturn[i] = high
        
        profit = 0
        
        for i in range(len(prices)):
            if maxReturn[i] - prices[i] > profit:
                profit = maxReturn[i] - prices[i]
            
        return profit
