class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fMap = defaultdict(int)
        for num in nums:
            fMap[num] += 1
        heapList = [(-y,x) for x,y in fMap.items()]
        heapq.heapify(heapList)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heapList)[1])
        return res
