class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l = 0
        r = len(height) - 1
        lmax = height[l]
        rmax = height[r]

        total = 0

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                total += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                total += rmax - height[r]
        return total

