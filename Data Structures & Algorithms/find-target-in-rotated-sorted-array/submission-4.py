class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        pivot = 0
        while l+1 < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid 
            else:
                r = mid
        pivot = r
        l,r = 0, len(nums)-1
        if nums[pivot] == target:
            return pivot
        elif nums[r] == target:
            return r
        elif nums[l] == target:
            return l
        if nums[pivot] < target and nums[r] > target:
            while pivot+1 < r:
                mid = (pivot+r) // 2
                if nums[mid] > target:
                    r = mid
                else:
                    pivot = mid
        else:
            pivot = pivot - 1
            while l+1 < pivot:
                mid = (l + pivot) // 2
                if nums[mid] > target:
                    pivot = mid
                else:
                    l = mid
        if nums[pivot] == target:
            return pivot
        elif nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        else:
            return -1

