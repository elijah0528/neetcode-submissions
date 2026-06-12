from collections import defaultdict, deque
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
            up, down, left, right
            eliminate invalid directions
            at i0, j0
            i1, j1 -> i0, j0
            i2
            

        """
        # Sizes
        N = len(matrix)
        M = len(matrix[0])
        def is_in_bounds(i, j):
            if 0 <= i < N and 0 <= j < M:
                return True
            return False
        directions  = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dp = [[None] * M for _ in range(N)]
        answer = 1
        seen = set()
        def search(i, j):
            """ Returns the next set of points """
            if dp[i][j] is not None:
                return dp[i][j]
            best = 1
            for di, dj in directions:
                if not is_in_bounds(i + di, j + dj):
                    continue
                if matrix[i][j] < matrix[i + di][j + dj]:
                    # Append the bigger cell to be searched
                    best = max(best, 1 + search(i + di, j + dj))
            dp[i][j] = best
            return best                
                        

        for i in range(N):
            for j in range(M):
                curr = search(i, j)
                print(curr)
                answer = max(answer, curr)
        return answer
                        
