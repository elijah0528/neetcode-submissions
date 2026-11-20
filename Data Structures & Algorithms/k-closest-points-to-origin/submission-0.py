import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        def distance(p1, p2):
            return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        
        for point in points:
            dist = distance(point, (0, 0))
            heapq.heappush(pq, (-dist, point))

            if len(pq) > k:
                heapq.heappop(pq)
            
        return [res[1] for res in pq]
