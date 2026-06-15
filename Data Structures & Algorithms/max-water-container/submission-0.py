class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l,r = 0 , len(heights) - 1
        while l < r:
            totalArea = 0
            if heights[l] > heights[r]:
                totalArea = heights[r] * (r - l)
                r -= 1
            else:
                totalArea = heights[l] * (r - l)
                l += 1
            if totalArea > maxArea:
                maxArea = totalArea

        return maxArea