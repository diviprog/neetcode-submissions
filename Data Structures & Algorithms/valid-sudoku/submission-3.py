class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        columns = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] in rows[i]: return False
                if board[i][j] in columns[j]: return False
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    columns[j].add(board[i][j])
        
        box = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
        boxes = [set() for i in range(9)]
        for box_i, box_j in box:
            for add_i, add_j in box:
                if board[3*box_i+add_i][3*box_j+add_j] in boxes[3*box_i+box_j]: return False
                if board[3*box_i+add_i][3*box_j+add_j] != '.':
                    boxes[3*box_i+box_j].add(board[3*box_i+add_i][3*box_j+add_j])
        
        return True
