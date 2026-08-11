class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            target = -num
            while l < r:
                tsum = nums[l] + nums[r]
                if tsum < target:
                    l += 1
                elif tsum > target:
                    r -= 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while l <r and nums[l] == nums[l-1]:
                        l +=1
        return res


        
            