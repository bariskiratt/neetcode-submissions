class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = [0] * 26
        for w in words:
            for c in w:
                freq[ord(c) - ord('a')] += 1
        for f in freq:
            if f > 0:
                if f % len(words) != 0:
                    return False
        return True