class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix) -1
        row = 0
        while l + 1 < r:
            mid = (l+r) // 2
            if matrix[mid][0] < target:
                l = mid
            elif matrix[mid][0] > target:
                r = mid
            else:
                return True
        if matrix[r][0] > target:
            row = l
        elif matrix[r][0] < target:
            row = r
        else:
            return True
        l,r = 0, len(matrix[row]) -1
        while l+1 < r:
            mid = (l+r) // 2
            if matrix[row][mid] < target:
                l = mid
            elif matrix[row][mid] > target:
                r = mid
            else:
                return True
        if matrix[row][l] == target:
            return True
        elif matrix[row][r] == target:
            return True
        return False
        