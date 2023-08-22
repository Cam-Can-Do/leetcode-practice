class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = [-count for count in counts.values()]
        heapq.heapify(maxHeap)
        q = deque()

        time = 0
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append([count, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
        
