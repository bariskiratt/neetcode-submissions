class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums:
            numSet.add(num)
        maxSequence = 0
        for num in nums:
            tempSequence = 1
            temp = num
            if num-1 not in numSet:
                while temp+1 in numSet:
                    tempSequence = tempSequence + 1
                    temp = temp + 1
                if tempSequence > maxSequence:
                    maxSequence = tempSequence
            
        return maxSequence
                
            
        