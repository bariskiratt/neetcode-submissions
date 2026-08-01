class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum = max(piles)
        l,r = 1 , maximum
        while l < r:
            count = 0
            mid = (l+r) // 2
            for num in piles:
                div,mod = divmod(num,mid)
                count += div if mod == 0 else div + 1
            if count <= h:
                r = mid
            elif count > h:
                l = mid+1
            else:
                return mid
        return l


