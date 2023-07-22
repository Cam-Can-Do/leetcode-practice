class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2
            timeUsed = 0
            for pile in piles:
                timeUsed += math.ceil(pile / m)
            if timeUsed <= h:
                r = m - 1
                res = min(res, m)
            else:
                l = m + 1
        return res

