class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0 , len(nums) -1
        index = -1
        while l < r:
            mid = (l+r) // 2
            if target < nums[mid]:
                r = mid
            elif target > nums[mid]:
                l = mid+1
            else:
                return mid
        if l == r and nums[l] == target:
            return l
            
        return -1
