class Solution:

    def longestPalindrome(self, s: str) -> str:
        # [i][j]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        # isPalindrome(i, j) if s[i] == s[j] AND (dp[i+1][j-1] OR j - i <= 2)
        res = ""
        if len(s) > 0:
            res = s[0]
        for length in range(2, len(s) + 1):
            for i in range(len(s) + 1 - length):
                j = i + length - 1
                if s[i] == s[j] and (length <= 3 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if length > len(res):
                        res = s[i: j + 1]
        return res
        
                

            