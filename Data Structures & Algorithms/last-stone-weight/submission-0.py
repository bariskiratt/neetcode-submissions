class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = abs(heapq.heappop(stones))
            y = abs(heapq.heappop(stones))
            if x == y:
                continue
            elif x < y:
                heapq.heappush(stones,x-y)
            else:
                heapq.heappush(stones,y-x)
        stones.append(0)
        return abs(stones[0])
            
