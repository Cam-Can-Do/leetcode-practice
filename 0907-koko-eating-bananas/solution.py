class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        res = r

        while l <= r:
            timeElapsed = 0
            m = (l + r) // 2
            for pile in piles:
                timeElapsed += ceil(pile / m)
            if timeElapsed <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res

        
