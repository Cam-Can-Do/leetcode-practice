class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first need to determine which row
        top = 0
        bottom = len(matrix) - 1
        row_len = len(matrix[0])
        row_ptr = 0
        while top <= bottom:
            row_ptr = (top + bottom) // 2 
            
            if matrix[row_ptr][0] <= target <= matrix[row_ptr][row_len - 1]:
                break   # found the correct row to conduct binary search on
            elif target > matrix[row_ptr][row_len - 1]:
                top = row_ptr + 1
            elif target < matrix[row_ptr][0]:
                bottom = row_ptr - 1
        
        if top > bottom:
            return False
        
        l = 0
        r = row_len - 1
        row = matrix[row_ptr]
        m = 0
        while l <= r:
            m = (l + r) // 2
            if row[m] == target:
                return True
            elif row[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False 
            

