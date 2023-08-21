class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for point in points:
            x = point[0]
            y = point[1]
            minHeap.append([(x ** 2 + y ** 2), x, y])
            
        res = []
        heapq.heapify(minHeap)
        for i in range(k):
            closest = heapq.heappop(minHeap)
            res.append([closest[1], closest[2]])
        return res

