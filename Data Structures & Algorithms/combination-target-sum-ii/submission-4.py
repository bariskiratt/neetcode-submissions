class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subset = []
        res = []
        candidates.sort()
        def backtrack(i,total):
            if total == target:
                res.append(subset.copy())
                return
            if total > target or i >= len(candidates):
                return

            total += candidates[i]
            subset.append(candidates[i])
            backtrack(i+1,total)

            total -= candidates[i]
            subset.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1,total)
        
        backtrack(0,0)
        return res