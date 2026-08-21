class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1] * len(nums)
        r = [1] * len(nums)
        product = 1
        res = []
        for i in range(0,len(nums)):
            product *= nums[i]
            l[i] = product
        product = 1
        for i in range(len(nums)-1,-1,-1):
            product *= nums[i]
            r[i] = product
        for i in range(len(nums)):
            if i == 0:
                res.append(1*r[i+1])
            elif i == len(nums)-1:
                res.append(l[i-1]*1)
            else:
                res.append(l[i-1]*r[i+1])
        return res
            

        