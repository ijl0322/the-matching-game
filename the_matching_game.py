import random

def showBoard(board):
    print "-"*17
    for line in board:
        board_line = "|"
        for item in line:
            if item[1]: 
                board_line += " " + item[0] + " " + "|"
            else:
                board_line += " " + " " + " " + "|"
        print "%s\n" %board_line, "-"*17
            
def init_board():
    board = []
    for i in range(4):
        board += [["O"]*4]

    item_list = [("A",False),("B",False),("C",False),("D",False),("E",False),\
    ("F",False),("G",False),("H",False),("A",False),("B",False),("C",False),("D",False),("E",False),\
    ("F",False),("G",False),("H",False)]
    
    for i in range(4):
        for j in range(4):
            item = item_list.pop(random.randrange(len(item_list)))
            board[i][j] = item
    return board
board = init_board()

showBoard(board)       
    