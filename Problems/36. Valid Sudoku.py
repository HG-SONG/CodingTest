class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(board):
            for row in board:
                visited = set()
                for item in row:
                    if item not in visited and item != ".":
                        visited.add(item)
                    elif item == ".":
                        continue
                    else:
                        return False
            return True

        def mask(board):
            for i in range(9):
                print(i)
                visited = set()
                for row in range(3):
                    for col in range(3):
                        print(row+3*(i//3),col + (3*(i%3)))
                        item = board[row+3*(i//3)][col + (3*(i%3))]
                        if item not in visited:
                            visited.add(item)
                        elif item == ".":
                            continue
                        else:
                            return False
            return True

        def transpose(board):
            return [list(row) for row in zip(*board)]

        check1 = checkRow(board)
        if check1 == False:
            return False

        trans = transpose(board)
        check2 = checkRow(trans)
        if check2 == False:
            return False

        if len(board) != 9 or len(trans) != 9:
            return False

        check3 = mask(board)
        if check3 == False:
            return False

        return check1 and check2 and check3