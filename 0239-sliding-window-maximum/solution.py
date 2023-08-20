class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        q = collections.deque()

        for i in range(len(nums)):
            if q and q[0] == i - k:
                q.popleft()
            while q and nums[q[len(q) - 1]] <= nums[i]:
                q.pop()
            
            q.append(i)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res



        
