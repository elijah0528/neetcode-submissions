class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = max(nums)
        for i in range(len(nums)):
            if nums[i] < 0:
                continue
            for j in range(i, len(nums)):
                if nums[j] < 0:
                    continue
                
                max_sum = max(max_sum, sum(nums[i:j + 1]))
        return max_sum