class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToLetter = {"2" : "abc","3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
        s = ""
        res = []
        if digits == "":
            return []
        def dfs(i):
            nonlocal s
            if i >= len(digits):
                res.append(s)
                return
            for j in range(0,len(numToLetter[digits[i]])):
                s += numToLetter[digits[i]][j]
                dfs(i+1)
                s = s[:-1]
        dfs(0)
        return res