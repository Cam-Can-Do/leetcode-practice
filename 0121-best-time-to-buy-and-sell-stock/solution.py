class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = prices[0]
        for price in prices:
            low = min(low, price)
            profit = max(profit, price - low)
        if profit < 0:
            profit = 0
        return profit

