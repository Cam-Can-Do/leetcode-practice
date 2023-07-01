class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        row_ptr = 0
        while top <= bottom:
            row_ptr = (top + bottom) // 2
            if target > matrix[row_ptr][len(matrix[row_ptr]) - 1]:
                top = row_ptr + 1
            elif target < matrix[row_ptr][0]:
                bottom = row_ptr - 1
            else:
                break
        if not (top <= bottom):
            return False

        row_ptr = (top + bottom) // 2
        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            col_ptr = (left + right) // 2
            if target > matrix[row_ptr][col_ptr]:
                left = col_ptr + 1
            elif target < matrix[row_ptr][col_ptr]:
                right = col_ptr - 1
            else:
                return True
        return False
