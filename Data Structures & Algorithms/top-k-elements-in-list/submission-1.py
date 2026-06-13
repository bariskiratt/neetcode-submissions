class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict()
        for num in nums:
            freq_map[num] = 1 + freq_map.get(num,0)
        freq = [[] for i in range(len(nums)+1)]
        for key,frequency in freq_map.items():
            freq[frequency].append(key)
        res = []
        for i in range(len(freq) - 1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

