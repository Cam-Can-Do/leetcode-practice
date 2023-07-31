class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        max_profit = 0

        for i in range(len(prices)):

            low = min(low, prices[i])

            max_profit = max(max_profit, prices[i] - low)
        return max_profit

