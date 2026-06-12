from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = k
        l = 0
        n = len(s)
        freq = defaultdict(int)
        max_count = -1
        for r in range(l, n):
            # Loop over substring exclusive of r
            freq[s[r]] += 1
            if freq[s[r]] > max_count:
                max_count = freq[s[r]]
            
            if r - l + 1 <= k + max_count:
                res = max(res, r - l + 1)
            else:
                while r - l + 1 > k + max_count:
                    freq[s[l]] -= 1
                    l += 1
        return res
            
 