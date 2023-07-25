class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = prices[0]
        
        for l in range(len(prices)):
            low = min(prices[l], low)
            profit = max(profit, prices[l] - low)
        if profit < 0:
            profit = 0
        return profit

