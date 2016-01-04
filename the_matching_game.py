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
    
def main():
    while True:
        clone_board = board[:]
        userGuess = raw_input("Enter 1st guess and 2nd guess:")
        clone_board[int(userGuess[0])][int(userGuess[1])] = \
        (clone_board[int(userGuess[0])][int(userGuess[1])][0], True)
        clone_board[int(userGuess[2])][int(userGuess[3])] = \
        (clone_board[int(userGuess[2])][int(userGuess[3])][0], True)
        
        showBoard(clone_board)
main()