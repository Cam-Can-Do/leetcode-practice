class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_contains = {}
        col_contains = {}

        # check rows and cols
        for i in range(0,9):
            for j in range(0,9):
                cur_in_row = board[i][j]
                if cur_in_row != ".":
                    if cur_in_row in row_contains:
                        return False
                    row_contains[cur_in_row] = True
                

                cur_in_col = board[j][i]
                if cur_in_col != ".":
                    if cur_in_col in col_contains:
                        return False
                    col_contains[cur_in_col] = True
            row_contains.clear()
            col_contains.clear()

        # need to check squares
        ranges = [range(0,3), range(3,6), range(6,9)]
        square_contains = {}

        # iterage over all ranges of indexes to check
        for i in range(0,3):
            for j in range(0,3):

                for x in ranges[i]:
                    for y in ranges[j]:
                        cur = board[x][y]
                        if cur != ".":
                            if cur in square_contains:
                                return False
                            square_contains[cur] = True
                square_contains.clear()

        return True
        
