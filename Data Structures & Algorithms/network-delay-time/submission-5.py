from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((t, v))
        pq = []
        heapq.heapify(pq)
        heapq.heappush(pq, (0, k))
        distances = [float('inf')] * (n + 1)
        distances[k] = 0
        while pq:
            curr_dist, curr = heapq.heappop(pq)
            if curr_dist > distances[curr]:
                continue
            print(curr_dist, curr)
            neighbours = adj[curr]
            for dist_new, new in neighbours:
                if curr_dist + dist_new < distances[new]:
                    distances[new] = curr_dist + dist_new
                    heapq.heappush(pq, (curr_dist + dist_new, new))
        distances = distances[1:]
        if max(distances) == float('inf'):
            return -1
        return max(distances)

