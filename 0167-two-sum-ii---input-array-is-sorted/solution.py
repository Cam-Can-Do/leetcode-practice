class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            tsum = numbers[l] + numbers[r]
            if tsum == target:
                return [l + 1, r + 1]
            elif tsum < target:
                l += 1
            else:
                r -= 1
        
