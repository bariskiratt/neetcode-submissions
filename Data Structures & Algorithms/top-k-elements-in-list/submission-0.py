class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = defaultdict()
        for num in nums:
            my_map[num] = 1 + my_map.get(num,0)
        heap = []
        for key in my_map.keys():
            heapq.heappush(heap, (my_map[key],key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res