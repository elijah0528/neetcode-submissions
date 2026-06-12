class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        seen = set(wordDict)
        sizes = set()
        for word in wordDict:
            sizes.add(len(word))


        for i in range(n - 1, -1, -1):
            for size in sizes:
                if i + size <= n and s[i: i + size] in seen and dp[i + size]:
                    dp[i] = True 

        return dp[0]
