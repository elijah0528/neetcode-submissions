class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        N = len(nums)
        res = []
        curr = []
        def dfs(left):
            if len(left) == 0:
                res.append(curr.copy())
                return

            for i in range(len(left)):
                curr.append(left[i])
                dfs(left[:i] + left[i + 1:])
                curr.pop()

        dfs(nums)
        return res