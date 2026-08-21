class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        fMap = defaultdict(int)
        res = []
        nums.sort()
        for num in nums:
            fMap[num] += 1
        for i in range(len(nums)):
            fMap[nums[i]] -= 1
            if i and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                fMap[nums[j]] -= 1
                if j-1>i and nums[j] == nums[j-1]:
                    continue
                left = -nums[i] - nums[j]
                if fMap[left] > 0 :
                    res.append([nums[i],nums[j],left])
            for j in range(i+1,len(nums)):
                fMap[nums[j]] += 1
        return res
