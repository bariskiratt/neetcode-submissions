class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res = []
        used = [False] * len(nums)
        def backtrack():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for j in range(len(nums)):
                if used[j]:
                    continue
                used[j] = True
                subset.append(nums[j])
                backtrack()
                subset.pop()
                used[j] = False
        backtrack()
        return res