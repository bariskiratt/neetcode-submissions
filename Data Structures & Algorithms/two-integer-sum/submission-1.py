class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        mymap = {}
        for i,num in enumerate(nums):
            left = target - num
            if left in mymap:
                return [mymap[left],i]
            mymap[num] = i
