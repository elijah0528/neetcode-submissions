class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # [1, 2, 3]
        # Choose 1 or not
        res = []
        curr = []
        def dfs(i):
            if i == len(nums):
                res.append(curr.copy())
                return
            dfs(i + 1) # Don't include current element

            curr.append(nums[i]) # Include this
            dfs(i + 1)
            curr.pop()


        dfs(0)
        return res
            
            