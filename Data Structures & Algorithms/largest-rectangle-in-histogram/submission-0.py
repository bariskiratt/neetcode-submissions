class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            width = 1
            for j in range(i-1,-1,-1):
                if heights[j] >= heights[i]:
                    width += 1
                else: 
                    break
            for k in range(i+1,len(heights)):
                if heights[k] >= heights[i]:
                    width += 1
                else:
                    break
            total = heights[i] * width
            if total > maxArea:
                maxArea = total
        return maxArea
