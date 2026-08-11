class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subset = []
        res = []
        def dfs(i,total):
            if total == target:
                res.append(subset.copy())
                return
            if total > target or i >= len(nums):
                return
            total += nums[i]
            subset.append(nums[i])
            dfs(i,total)
            total -= nums[i]
            subset.pop()
            dfs(i+1,total)
        dfs(0,0)
        return res