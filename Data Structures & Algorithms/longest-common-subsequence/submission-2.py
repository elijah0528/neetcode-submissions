class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp
        #   c a t
        # c 1 2  0
        # r   2 0
        # a   2 0 
        # b   0 0
        # t   0 1
        dp = [[0] * len(text2) for _ in range(len(text1))]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                right = down = 0
                if 0 <= i + 1 < len(text1):
                    down = dp[i + 1][j]
                if 0 <= j + 1 < len(text2):
                    right = dp[i][j + 1]
                curr = max(right, down)
                if text1[i] == text2[j]:
                    diag = dp[i + 1][j + 1] if 0 <= i + 1 < len(text1) and 0 <= j + 1 < len(text2) else 0
                    dp[i][j] = 1 + diag
                else:
                    dp[i][j] = curr

        return dp[0][0]
