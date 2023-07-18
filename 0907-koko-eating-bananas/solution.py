class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # n <= h 
        # need to search for the correct k value (binary search) between 1 and max(piles)
        # for each k value, need to check whether the time consumed is less than or equal to h
        # store valid k values but continue searching while valid for lowest valid 

        low = 1
        high = max(piles)
        res = high

        while low <= high:
            speed = (low + high) // 2 
            timeUsed = 0
            for pile in piles:
                timeUsed += math.ceil(pile / speed)
            if timeUsed <= h:
                res = min(res, speed)
                high = speed - 1
            else:
                low = speed + 1
        return res 


                


