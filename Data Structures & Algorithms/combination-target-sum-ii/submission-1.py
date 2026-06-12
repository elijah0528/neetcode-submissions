class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curr = []

        def dfs(i, remaining):
            if remaining == 0:
                res.append(curr.copy())
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if candidates[j] > remaining:
                    break
                curr.append(candidates[j])
                dfs(j + 1, remaining - candidates[j])
                curr.pop()
        
        dfs(0, target)
        return res

