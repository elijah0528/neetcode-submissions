class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        If s1[0] or s2[0] == s3[0]:
            consume char
        If s1[0] and s2[0] == s3[0]:
            create 2 paths and evaluate both
        """
        dp = [[None] * (len(s1) + 1) for _ in range(len(s2) + 1)]
        size_of_s1 = len(s1)
        size_of_s2 = len(s2)
        size_of_s3 = len(s3)
        if size_of_s1 + size_of_s2 != size_of_s3:
            return False
        def dfs(i, j, k):
            l = r = False
            # try:
            if (i == size_of_s1 and 
                j == size_of_s2 and 
                k == size_of_s3):
                return True
            # Cached
            if dp[i][j] is not None:
                return dp[i][j]
            if i < size_of_s1 and s1[i] == s3[k]:
                l = dfs(i + 1, j, k + 1)
                dp[i][j] = l
            if j < size_of_s2 and s2[j] == s3[k]:
                r = dfs(i, j + 1, k + 1)
                dp[i][j] = r
            """
            except Exception as e:
                print(f"I: {i}, J: {j}, K: {k}")
                print(e)
                return False
            """
            return l or r
        res = dfs(0, 0, 0)
        return res