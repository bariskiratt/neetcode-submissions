class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        maxNum = 0
        res = 0

        for i,num in enumerate(height):
            if i == 0:
                maxNum = height[i]
                continue
            if height[i] > maxNum:
                maxLeft[i] = maxNum
                maxNum = height[i]
            else:
                maxLeft[i] = maxNum


        for i in range(len(height) -1, -1 , -1):
            if i == len(height) -1:
                maxNum = height[i]
                continue
            if height[i] > maxNum:
                maxRight[i] = maxNum
                maxNum = height[i]
            else:
                maxRight[i] = maxNum


        for i,num in enumerate(height):
            trapped = min(maxLeft[i],maxRight[i]) - height[i]
            if trapped > 0:
                res+= trapped
        return res

            