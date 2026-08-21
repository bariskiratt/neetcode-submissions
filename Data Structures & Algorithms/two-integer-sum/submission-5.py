class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}
        for i,num in enumerate(nums):
            if target - num in hMap:
                return [hMap[target-num],i]
            hMap[num] = i
        