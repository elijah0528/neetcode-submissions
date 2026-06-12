from collections import Counter

class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        def char_freq(s: str):
            return Counter(s)
        count = char_freq(s1)
        for l in range(n - m + 1):
            curr_count = count.copy()
            remaining = m
            r = l
            while r < len(s2) and r < l + len(s1):
                if curr_count[s2[r]] > 0:
                    curr_count[s2[r]] -= 1
                    remaining -= 1
                    r += 1
                else:
                    break
                if remaining == 0:
                    return True
        return False
