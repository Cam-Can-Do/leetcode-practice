class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            s1 = abs(heapq.heappop(maxHeap))
            s2 = abs(heapq.heappop(maxHeap))
            if s1 != s2:
                heapq.heappush(maxHeap, -(max(s1, s2) - min(s1, s2)))
        if len(maxHeap) == 0:
            return 0
        else:
            return abs(maxHeap[0])

        
