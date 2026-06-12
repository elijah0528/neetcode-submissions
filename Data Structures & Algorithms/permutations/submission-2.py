class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        N = len(nums)
        used = [False] * len(nums)
        res = []
        curr = []
        def dfs():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(used)):
                if used[i]:
                    continue
                curr.append(nums[i])
                used[i] = True
                dfs()
                used[i] = False
                curr.pop()

        dfs()
        return res