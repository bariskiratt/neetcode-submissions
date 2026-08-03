class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0 , len(nums)-1
        if l == r and nums[l] == target:
            return l
        pivot = 0
        res = 0
        while l < r:
            if nums[l] < nums[r]:
                pivot = l
                break
            mid = (l+r) // 2
            if nums[mid] > nums[mid+1]:
                pivot = mid+1
                break
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid+1
        nums = nums[pivot:len(nums)] + nums[0:pivot]
        l,r = 0 , len(nums)-1
        while l <= r :
            mid = (l+r) // 2
            if nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid-1
            else:
                if (pivot + mid) >= len(nums):
                    return pivot + mid - len(nums)
                else:
                    return pivot + mid
        return -1 

