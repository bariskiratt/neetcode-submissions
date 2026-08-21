class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = defaultdict(int)
        for num in nums:
            if num in hashMap:
                return True
            hashMap[num] = 1
        return False
