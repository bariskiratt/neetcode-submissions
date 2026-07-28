class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        bestBuy = prices[0]
        for sell in prices:
            maxP = max(maxP,sell-bestBuy)
            bestBuy = min(bestBuy,sell)
        return maxP