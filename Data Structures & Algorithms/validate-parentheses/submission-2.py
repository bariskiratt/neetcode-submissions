class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {'(' : ')', '[' : ']' , '{' : '}'}
        arr = []
        for ch in s:
            if ch in openToClose:
                arr.append(ch)
            else:
                if not arr:
                    return False
                if(openToClose[arr[-1]] == ch):
                    arr.pop()
                else:
                    return False
        return True if not arr else  False


                
