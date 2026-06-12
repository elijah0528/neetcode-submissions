class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Brute force
        # Generate all subsets of nums
        # If a subset is equal to half the sum of nums then return True
        # Optimization: If curr_sum goes past half, stop dfs
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s // 2
        
        res = []
        curr = []
        def dfs(i):
            # Either choose to take first element or not
            if sum(curr) > target:
                return
            if sum(curr) == target:
                res.append(curr.copy())            
            if i == len(nums):
                return
            
            dfs(i + 1)
            curr.append(nums[i])
            dfs(i + 1)
            curr.pop()

            return 
        dfs(0)
        print(res) 
        return True if res else False