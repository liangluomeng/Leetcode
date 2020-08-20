# -*- coding:utf-8 -*-

class debug():
    def updateBoard(board, click):
        click_square = board[click[0]][click[1]]
        output = board

        if len(board) == 1:
            if board[0][0] == "E":
                return [["B"]]
            elif board[0][0] == "M":
                return [["X"]]

        def surroundingSquares(pos):
            len_x = len(board) - 1
            len_y = len(board[0]) - 1
            x = pos[0]
            y = pos[1]
            if len_x == 0 or len_y == 0:
                if len_x == 0:
                    if y == 0:
                        out = [[0, 1]]
                    elif y == len_y:
                        out = [[0, y - 1]]
                    else:
                        out = [[0, y - 1], [0, y + 1]]
                elif len_y == 0:
                    if x == 0:
                        out = [[1, 0]]
                    elif x == len_x:
                        out = [[x - 1, 0]]
                    else:
                        out = [[x - 1, 0], [x + 1, 0]]
            else:
                if x == 0:
                    if y == 0:
                        out = [[0, 1], [1, 0], [1, 1]]
                    elif y == len_y:
                        out = [[0, y - 1], [1, y - 1], [1, y]]
                    else:
                        out = [[0, y - 1], [0, y + 1], [1, y - 1], [1, y], [1, y + 1]]
                elif x == len_x:
                    if y == 0:
                        out = [[x - 1, 0], [x - 1, 1], [x, 1]]
                    elif y == len_y:
                        out = [[x - 1, y - 1], [x - 1, y], [x, y - 1]]
                    else:
                        out = [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1], [x, y - 1], [x, y + 1]]
                elif y == 0:
                    out = [[x - 1, y], [x - 1, y + 1], [x, y + 1], [x + 1, y], [x + 1, y + 1]]
                elif y == len_y:
                    out = [[x - 1, y - 1], [x - 1, y], [x, y - 1], [x + 1, y - 1], [x + 1, y]]
                else:
                    out = [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1], [x, y - 1], [x, y + 1], [x + 1, y - 1], [x + 1, y],
                           [x + 1, y + 1]]
            return out

        def numberOfMines(pos):
            mine_count = 0
            all_pos = surroundingSquares(pos)
            all_pos.insert(0,pos)
            for i in range(len(all_pos)):
                if board[all_pos[i][0]][all_pos[i][1]] == "M":
                    mine_count += 1
            return mine_count

        def revealSquare(click):
            relavent_pos = surroundingSquares(click)
            for pos_selected in relavent_pos:
                if board[pos_selected[0]][pos_selected[1]] != "E":
                    continue
                if numberOfMines(pos_selected) == 0:
                    output[pos_selected[0]][pos_selected[1]] = "B"
                    append_quare = surroundingSquares(pos_selected)
                    for pos_append in append_quare:
                        if pos_append not in relavent_pos:
                            relavent_pos.append(pos_append)
                elif numberOfMines(pos_selected) != 0:
                    output[pos_selected[0]][pos_selected[1]] = str(numberOfMines(pos_selected))


        if click_square == "M":
            output[click[0]][click[1]] = "X"
        elif click_square == "E":
            if numberOfMines(click) == 0:
                output[click[0]][click[1]] = "B"
                revealSquare(click)
            else:
                output[click[0]][click[1]] = str(numberOfMines(click))

        return output



    if __name__ == '__main__':
        print(updateBoard([["M"],["M"],["E"],["M"],["E"]],[2,0]))