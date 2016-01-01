import random

board = []
for i in range(4):
    board += [["O"]*4]


def showboard(board):
    print "-"*17
    for line in board:
        board_line = "|"
        for item in line:
            board_line += " " + item[0] + " " + "|"
        print "%s\n" %board_line, "-"*17
            
def init_board(board):
    item_list = [("A",False),("B",False),("C",False),("D",False),("E",False),\
    ("F",False),("G",False),("H",False),("A",False),("B",False),("C",False),("D",False),("E",False),\
    ("F",False),("G",False),("H",False)]
    for i in range(4):
        for j in range(4):
            item = item_list.pop(random.randrange(len(item_list)))
            board[i][j] = item
init_board(board)
showboard(board)       
    