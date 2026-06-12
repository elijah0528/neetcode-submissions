from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # [-2, ]
        results = defaultdict(int)
        results[0] = 1
        for i in range(len(nums)):
            pos = nums[i]
            neg = -1 * nums[i]
            new_set = defaultdict(int)
            for k, v in results.items():
                if k + pos not in new_set:
                    new_set[k + pos] = v
                else:
                    new_set[k + pos] += v
                if k + neg not in new_set:
                    new_set[k + neg] = v
                else:
                    new_set[k + neg] += v
            print(new_set)
            results = new_set
        return results[target]
        

