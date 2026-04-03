class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            valid = set()
            for num in row:
                if num == ".":
                    continue
                if num in valid:
                    return False
                valid.add(num)

        for column in range(9):
            valid = set()
            for row in range(9):
                if board[row][column] == ".":
                    continue
                if board[row][column] in valid:
                    return False
                valid.add(board[row][column])
        
        for row in range(0,9,3):
            for column in range(0,9,3):
                valid = set()
                for r in range(0,3,1):
                    for c in range (0,3,1):
                        if board[row+r][column+c] == ".":
                            continue

                        if board[row+r][column+c] in valid:
                            return False

                        valid.add(board[row+r][column+c])
                

        return True

        