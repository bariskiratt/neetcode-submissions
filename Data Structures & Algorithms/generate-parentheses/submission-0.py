class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(s,openBrackets,formedParantheses):
            if formedParantheses == n:
                res.append(s)
                return
            if openBrackets > 0:
                if formedParantheses + openBrackets >= n:
                    backtrack(s+")",openBrackets-1,formedParantheses+1)
                else:
                    backtrack(s+"(",openBrackets+1,formedParantheses)
                    backtrack(s+")",openBrackets-1,formedParantheses+1)
            else:
                backtrack(s+"(",openBrackets+1,formedParantheses)
        backtrack("",0,0)
        return res