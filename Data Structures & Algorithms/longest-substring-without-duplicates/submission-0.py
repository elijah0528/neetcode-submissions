from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        res = 0
        l = r = 0
        while r < len(s):
            if freq[s[r]] == 0:
                freq[s[r]] += 1
                r += 1
                res = max(res, r - l)
            else:
                freq[s[l]] -= 1
                l += 1
        return res
