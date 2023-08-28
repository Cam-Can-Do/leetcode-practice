class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]

        res = 0
        for price in prices:
            low = min(low, price)
            res = max(res, price - low)
        return res
        
