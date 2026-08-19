class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(s,closed,opened):
            if len(s) == 2 *n:
                res.append(s)
                return
            if opened < n:
                backtrack(s+"(",closed,opened+1)
            if closed < opened:
                backtrack(s + ")", closed+1, opened)
        backtrack("",0,0)
        return res