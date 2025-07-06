class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Validate rows
        for i in range(9):
            h = set()
            for j in range(9):
                if board[i][j] in h:
                    return False
                elif board[i][j] != ".":
                    h.add(board[i][j])

        # Validate columns
        for i in range(9):
            h = set()
            for j in range(9):
                if board[j][i] in h:
                    return False
                elif board[j][i] != ".":
                    h.add(board[j][i])

        # validate each 3 x 3 box
        boxes = [
            (0,0), (0,3), (0,6),
            (3,0), (3,3), (3,6),
            (6,0), (6,3), (6,6)
        ]

        for i,j in boxes:
            h = set()
            for row in range(i, i+3):
                for column in range(j, j+3):
                    if board[row][column] in h:
                        return False
                    elif board[row][column] != ".":
                        h.add(board[row][column])
        return True