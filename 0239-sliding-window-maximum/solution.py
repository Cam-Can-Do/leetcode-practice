class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        res = []
        for i in range(len(nums)):
            if dq and dq[0] == i - k:
                dq.popleft()
            while dq and nums[dq[len(dq) - 1]] <= nums[i]:
                dq.pop()
            
            dq.append(i)
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res
        
