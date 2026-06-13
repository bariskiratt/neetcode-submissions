class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        for i,num1 in enumerate(nums):
            left = target - num1
            for j,num2 in enumerate(nums):
                if (i != j) and (num2 == left):
                    return [i,j]
