class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
                continue
            seen.add(num)

        res = list(seen)[0]
        return res