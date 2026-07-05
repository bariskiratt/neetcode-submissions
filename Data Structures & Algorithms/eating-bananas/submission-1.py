class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minRate = 1000
        maxVal = 0
        for i in range(len(piles)):
            if piles[i] > maxVal:
                maxVal = piles[i]
        l,r = 1,maxVal
        while l+1 < r:
            mid = (l+r) // 2
            hourCtr = 0
            for val in piles:
                hourCtr += (val // mid) if val % mid == 0 else (val // mid + 1)
            if hourCtr <= h:
                r = mid
            elif hourCtr > h:
                l = mid
            if hourCtr <= h:
                minRate = mid
        hourCtr = 0
        for val in piles:
            hourCtr += (val // l) if val % l ==0 else (val // l + 1)
        if hourCtr <= h:
            minRate = min(minRate,l)
        hourCtr = 0
        for val in piles:
            hourCtr += (val // r) if val % r ==0 else (val // r + 1)
        if hourCtr <= h:
            minRate = min(minRate,r)
        return minRate

