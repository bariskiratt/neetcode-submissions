class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        res = 0
        for num in prices:
            minBuy = min(minBuy,num)
            res = max(res,num-minBuy)
        return res
