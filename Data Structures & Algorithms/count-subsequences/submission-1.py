class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[None] * len(t) for _ in range(len(s))]
        def dfs(s_curr: int, t_curr: int) -> int:
            # We have a full word matched
            if t_curr == len(t):
                return 1
            if s_curr == len(s):
                return 0
            if dp[s_curr][t_curr] is not None:
                return dp[s_curr][t_curr]
            # Get the current s letter
            s_char = s[s_curr]
            target = t[t_curr]
            if s_char == target:
                take_char = dfs(s_curr + 1, t_curr + 1)
                leave_char = dfs(s_curr + 1, t_curr)
            else:
                take_char = 0
                leave_char = dfs(s_curr + 1, t_curr)  
            res = take_char + leave_char
            dp[s_curr][t_curr] = res
            return res     
        
        res = dfs(0, 0)
        return res
