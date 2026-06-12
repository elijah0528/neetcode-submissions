from collections import deque
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for i in range(m):
            arr = []
            for j in range(n):
                arr.append(0)
            dp.append(arr)
        dp[m - 1][n - 1] = 1

        # Up and left
        directions = [(-1, 0), (0, -1)]
        checks = [(1, 0), (0, 1)]
        start = (m - 1, n - 1)
        q = deque([start])

        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                res = 0
                for dx, dy in directions:
                    if 0 <= x + dx < m and 0 <= y + dy < n:
                        q.append((x + dx, y + dy))
                for cx, cy in checks:
                    if 0 <= x + cx < m and 0 <= y + cy < n:
                        res += dp[x + cx][y + cy]
                dp[x][y] = max(dp[x][y], res)
        return dp[0][0]
