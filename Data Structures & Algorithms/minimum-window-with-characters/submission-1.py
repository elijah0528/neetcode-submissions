from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def sContainsT(s_dict, t_dict):
            for k, v in t_dict.items():
                # Has less than v elems
                if s_dict[k] < v:
                    return False
            return True

        def getCount(s: str):
            return Counter(s)

        l = r = 0
        needed = getCount(t)
        required = len(needed)
        res = ""
        window = defaultdict(int)
        formed = 0
        best_len = float("inf")
        best_l = 0
        while r < len(s):
            ch = s[r]
            if ch in needed:
                window[ch] += 1
                if window[ch] == needed[ch]:
                    formed += 1 # Got all the values for a char
            r += 1
            while formed == required:
                if r - l < best_len:
                    best_len = r - l
                    best_l = l

                left = s[l]
                if left in needed:
                    window[left] -= 1
                    if window[left] < needed[left]:
                        formed -= 1
                l += 1

        return "" if best_len == float('inf') else s[best_l:best_l + best_len]

            
