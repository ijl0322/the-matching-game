import random
from copy import deepcopy

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
        
def checkWin(board):
    score = 0
    for line in board:
        for item in line:
            if item[1] == True:
                score += 1
    return score == 16
                
            
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
    numTry = 0
    while not checkWin(board):
        numTry += 1
        print "\nNum of Trials: ", numTry

        clone_board = deepcopy(board)
        userGuess = raw_input("Enter 1st guess and 2nd guess:")  
        for guess in userGuess:
            invalid = False  
            if guess not in ["0","1","2","3"]:                
                invalid = True
        if invalid:
            print "Invalid Input. Please try again"
            continue
                
        clone_board[int(userGuess[0])][int(userGuess[1])] = \
        (clone_board[int(userGuess[0])][int(userGuess[1])][0], True)
        clone_board[int(userGuess[2])][int(userGuess[3])] = \
        (clone_board[int(userGuess[2])][int(userGuess[3])][0], True)
        
        if clone_board[int(userGuess[0])][int(userGuess[1])][0] == clone_board[int(userGuess[2])][int(userGuess[3])][0]:
            board[int(userGuess[0])][int(userGuess[1])] = clone_board[int(userGuess[0])][int(userGuess[1])]
            board[int(userGuess[2])][int(userGuess[3])] = clone_board[int(userGuess[2])][int(userGuess[3])]
        
        
        showBoard(clone_board)
        
    print "Congratulations! You win!"
    
main()