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

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1 , -1):
                if i == m - 1 and j == n - 1:
                    continue
                down = right = 0
                # Down
                if 0 <= i + 1 < m:
                    down = dp[i + 1][j]
                # Right
                if 0 <= j + 1 < n:
                    right = dp[i][j + 1]

                dp[i][j] = max(dp[i][j], down + right)
        return dp[0][0]
