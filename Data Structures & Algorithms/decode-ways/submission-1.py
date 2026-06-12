class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s) + 1)]
        dp[len(s)] = 1

        dp[len(s) - 1] = 1 if s[-1] != '0' else 0
        # 12132112
        # If new i can concatenate its new_i + dp[i + 2]
        # If not then new_i + dp[i]
        print(dp)
        for i in range(len(s) - 2, -1, -1):
            if s[i] == '0':
                dp[i] = 0
                continue
            dp[i] = dp[i + 1]
            if 0 <= int(s[i: i + 2]) <= 26:
                dp[i] += dp[i + 2]

        return dp[0]

