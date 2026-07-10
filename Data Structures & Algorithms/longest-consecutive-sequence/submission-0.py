class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        mp = defaultdict(int)

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1

                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]

                res = max(res, mp[num])

        return res
