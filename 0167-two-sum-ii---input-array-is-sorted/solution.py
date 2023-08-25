class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            leftVal = numbers[l] 
            rightVal = numbers[r]
            two_sum = leftVal + rightVal

            if two_sum == target:
                return [l+1, r+1]
            elif two_sum < target:
                l += 1
            else:
                r -= 1

