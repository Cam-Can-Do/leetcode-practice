class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search with eating speeds for the lowest valid eating speed
        # that allows koko to eat all bananas before guards return

        l = 1 # starts at 1 because 0 bananas will get nothing done...
        r = max(piles)
                            
        res = r
        while l <= r:
            m = (l + r) // 2
            time = 0
            for pile in piles:
                time += ceil(pile / m)
            if time <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
            
