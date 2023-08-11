class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        row_len = len(matrix[0])
        row = []
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] <= target <= matrix[mid][row_len - 1]:
                row = matrix[mid]
                break
            elif target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][row_len - 1]:
                top = mid + 1
        
        if not row:
            return False

        l = 0
        r = row_len - 1
        while l <= r:
            m = (l + r) // 2
            if row[m] == target:
                return True
            elif target < row[m]:
                r = m - 1
            else:
                l = m + 1
        return False


        
        
