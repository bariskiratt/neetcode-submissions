class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f1 = [0] * 26
        f2 = [0] * 26
        for c in s:
            f1[ord(c) - ord("a")] += 1
        for c in t:
            f2[ord(c)- ord("a")] += 1
        return f1 == f2