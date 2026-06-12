class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        curr = []
        def dfs(start_ind, remaining):
            if remaining == 0:
                res.append(curr.copy())
                return
            for i in range(start_ind, len(nums)):
                if remaining - nums[i] < 0:
                    return 
                curr.append(nums[i])
                dfs(i, remaining - nums[i])
                curr.pop()


        dfs(0, target)
        return res