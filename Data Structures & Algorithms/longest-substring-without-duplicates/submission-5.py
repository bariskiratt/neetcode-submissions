class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = defaultdict(int)
        l = 0
        maxCount = 0
        for r in range(len(s)):
            if s[r] not in hashMap:
                hashMap[s[r]] += 1
            else:
                while hashMap[s[r]] > 0 and l < r:
                    hashMap[s[l]] -= 1
                    l += 1
                hashMap[s[r]] += 1
            maxCount = max(maxCount,r-l+1)
        return maxCount
                    