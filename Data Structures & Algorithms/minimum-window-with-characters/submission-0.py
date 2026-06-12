from collections import Counter
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
        t_dict = getCount(t)
        res = ""
        while r <= len(s) and l < len(s):
            s_dict = getCount(s[l:r])
            if sContainsT(s_dict, t_dict):
                if res == "":
                    res = s[l:r]
                elif len(res) > len(s[l:r]):
                    res = s[l:r]
                l += 1
            else:
                r += 1
        return res

            
