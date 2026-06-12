class Solution:
    def isPalindrome(self, s: str):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    def partition(self, s: str) -> List[List[str]]:
        # aab
        # a ab
        res = []
        curr = []
        def dfs(start):
            if start == len(s):
                res.append(curr.copy())
                return
            for i in range(start, len(s)):
                word = s[start:i + 1]
                if not self.isPalindrome(word):
                    continue
                curr.append(word)
                dfs(i + 1)
                curr.pop()
        dfs(0)
        return res