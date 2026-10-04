class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        fMap = defaultdict(list)
        for word in strs:
            idStr = [0] * 26
            for c in word:
                idStr[ord(c) - ord('a')] += 1
            fMap[tuple(idStr)].append(word)
        return list(fMap.values())