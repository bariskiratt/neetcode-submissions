class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        while l+1 < r:
            mid = (l+r) // 2
            if nums[mid] > nums[l]:
                l = mid
            elif nums[mid] < nums[r]:
                r = mid
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
        if nums[l] > nums[r]:
            return nums[r]
        else:
            return nums[0]