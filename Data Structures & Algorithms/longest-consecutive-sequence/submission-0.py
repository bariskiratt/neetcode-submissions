class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums:
            numSet.add(num)
        maxSequence = 0
        for num in nums:
            tempSequence = 1
            temp = num
            while temp+1 in numSet:
                tempSequence = tempSequence + 1
                temp = temp + 1
            if tempSequence > maxSequence:
                maxSequence = tempSequence
            
        return maxSequence
                
            
        