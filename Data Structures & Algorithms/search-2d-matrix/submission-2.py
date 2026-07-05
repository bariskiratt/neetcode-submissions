class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix), len(matrix[0])
        l,r = 0, rows * cols - 1
        while l + 1 < r:
            mid = (l+r) // 2
            midRow = mid // cols
            midCols = mid % cols
            if matrix[midRow][midCols] < target:
                l = mid
            elif matrix[midRow][midCols] > target:
                r = mid
            else:
                return True
        if matrix[l//cols][l%cols] == target:
            return True
        elif matrix[r//cols][r%cols] == target:
            return True
        return False
