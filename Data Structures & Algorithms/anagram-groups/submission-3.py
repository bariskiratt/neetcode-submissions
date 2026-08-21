class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hMap = defaultdict(list)
        for s in strs:
            fMap = [0] * 26
            for c in s:
                fMap[ord(c) - ord("a")] += 1
            hMap[tuple(fMap)].append(s)
        for maps in hMap.values():
            res.append(maps)
        return res


