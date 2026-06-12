from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # [-2, ]
        dp = defaultdict(int)
        dp[0] = 1
        for i in range(len(nums)):
            pos = nums[i]
            neg = -1 * nums[i]
            next_dp = defaultdict(int)
            for k, v in dp.items():
                next_dp[k + pos] += v
                next_dp[k + neg] += v
            dp = next_dp
        return dp[target]
        

