class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxProfit = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit,profit)
            if (l+1 < r and prices[l+1] < prices[l]) or (l+1 < r and prices[r] < prices[l]) :
                l += 1
            else:
                r += 1
        return maxProfit


