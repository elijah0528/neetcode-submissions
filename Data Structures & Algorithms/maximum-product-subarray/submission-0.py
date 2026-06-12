class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # [1, 2, -3, 4]
        res = max_val = min_val = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            new_subarr = num
            mult_max = num * max_val
            mult_min = num * min_val
            max_val = max(new_subarr, mult_max, mult_min)
            min_val = min(new_subarr, mult_max, mult_min)
            res = max(res, max_val)

        return res