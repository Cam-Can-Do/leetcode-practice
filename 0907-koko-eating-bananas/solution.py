class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2
            timeElapsed = 0
            for pile in piles:
                timeElapsed += math.ceil(pile / m)
            # valid speed
            if timeElapsed <= h:
                r = m - 1
                res = min(res, m)
            else:
                l = m + 1

        return res
            
        
