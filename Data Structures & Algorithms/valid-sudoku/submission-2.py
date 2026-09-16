class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(row):
            num_row = [x for x in row if x != "."]
            return len(num_row) == len(set(num_row))
        
        for i in range(9):
            if not isValid(board[i]):
                return False
            col = [board[r][i] for r in range(9)]
            if not isValid(col):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [row[j:j+3] for row in board[i:i+3]]
                box_arr = [item for subarray in box for item in subarray]
                if not isValid(box_arr):
                    return False
        return True