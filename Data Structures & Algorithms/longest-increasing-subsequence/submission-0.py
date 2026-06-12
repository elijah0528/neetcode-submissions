class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # []
        dp = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            vals = []
            for j in range(i,len(nums)):
                if nums[i] < nums[j]:
                    vals.append(dp[j])
            if vals:
                dp[i] = max(dp[i], *[1 + val for val in vals])
        return max(dp)
