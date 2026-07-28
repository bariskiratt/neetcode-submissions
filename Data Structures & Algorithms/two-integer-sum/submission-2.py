class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        hashMap = {}
        for i,num in enumerate(nums):
            left = target - num
            if left in hashMap:
                return [hashMap[left],i]
            hashMap[num] = i
        
