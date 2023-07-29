class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        # binary search for lowest valid speed
        while l <= r:
            speed = (l + r) // 2
            timeElapsed = 0
            for pile in piles:
                timeElapsed += math.ceil(pile / speed)
            # valid speed, but want to keep searching for lower... move right pointer
            if timeElapsed <= h:
                res = min(speed, res)
                r = speed - 1
            # timeElapsed > h ... took too long... need to increase speed by increasing left pointer
            else:
                l = speed + 1
        return res


        
