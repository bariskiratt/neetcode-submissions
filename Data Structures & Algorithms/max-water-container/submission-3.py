class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0 , len(heights)-1
        maxWater = 0
        while l < r:
            total = (r-l) * min(heights[l],heights[r])
            if min(heights[l],heights[r]) == heights[l]:
                l += 1
            elif min(heights[l],heights[r]) == heights[r]:
                r -= 1
            maxWater = max(maxWater,total)
        return maxWater                