class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        seen = set()
        l,r = 0,0
        seen.add(s[l])
        longest = 1
        res = 1
        while r < len(s)-1:
            r += 1
            longest += 1
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1 
                    longest -= 1
            seen.add(s[r])
            res = max(res,longest)
        return res

