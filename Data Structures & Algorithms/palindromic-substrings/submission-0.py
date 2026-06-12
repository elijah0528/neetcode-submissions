class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
        
        count = len(s)
        # String of size 2 to N
        for str_len in range(2, n + 1):
            for i in range(n - str_len + 1):
                j = i + str_len - 1
                if s[i] == s[j] and (str_len <= 3 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    count += 1

        return count