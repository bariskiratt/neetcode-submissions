class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()
        subset = []
        def backtrack():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            for i,num in enumerate(nums):
                if i in used:
                    continue
                used.add(i)
                subset.append(num)
                backtrack()
                subset.pop()
                used.remove(i)
        backtrack()
        return res