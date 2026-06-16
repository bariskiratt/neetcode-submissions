class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxRight = [0] * len(prices)
        maxNum = 0
        for i in range(len(prices)-1,-1,-1):
            if prices[i] > maxNum:
                maxNum = prices[i]
            maxRight[i] = maxNum
        maxProfit = 0
        for i in range(len(prices)-1):
            profit = maxRight[i] - prices[i]
            if profit> maxProfit:
                maxProfit = profit
        return maxProfit


        
