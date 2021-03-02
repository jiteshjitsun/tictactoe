class color:
    BOLD = '\033[1m'

def play_again():
    X = input("Enter the name of X player:  ")
    O = input("Enter the name of O player:  ")
    n=0
    while n != 1:
        name = input("Who wants to go first {} or {}:  ".format(X,O))
        if name==X or name==O:
            print("{} will go first: ".format(name))
            n=1
        else:
            print("***ERROR***\n")
            print("{} is not registered with us:".format(name))
    board = {
        '00':'.','01':'.','02':'.','10':'.',
        '11':'.','12':'.','20':'.','21':'.','22':'.'}
    def check():
        if board['00'] == 'X' and board['01'] == 'X' and board['02'] == 'X':
            print("Game is over:")
            print('{} won !'.format(X))
            return 1
        if board['10'] == 'X' and board['11'] == 'X' and board['12'] == 'X':
            print("Game is over:")
            print('{} won !'.format(X))
            return 1
        if board['20'] == 'X' and board['21'] == 'X' and board['22'] == 'X':
            print("Game is over:")
            print('{} won !'.format(X))
            return 1
        if board['00'] == 'X' and board['11'] == 'X' and board['22'] == 'X':
            print("Game is over:")
            print('{} won !'.format(X))
            return 1
        if board['00'] == 'X' and board['10'] == 'X' and board['20'] == 'X':
            print("Game is over:")
            print('{} won !'.format(X))
            return 1
        if board['01'] == 'X' and board['11'] == 'X' and board['21'] == 'X':
            print("Game is over:")
            print('{} won !'.format(X))
            return 1
        if board['02'] == 'X' and board['12'] == 'X' and board['22'] == 'X':
            print("Game is over:")
            print('{} won !'.format(X))
            return 1
        if board['00'] == 'O' and board['01'] == 'O' and board['02'] == 'O':
            print("Game is over:")
            print('{} won !'.format(O))
            return 1 
        if board['10'] == 'O' and board['11'] == 'O' and board['12'] == 'O':
            print("Game is over:")
            print('{} won !'.format(O))
            return 1
        if board['20'] == 'O' and board['21'] == 'O' and board['22'] == 'O':
            print("Game is over:")
            print('{} won !'.format(O))
            return 1
        if board['00'] == 'O' and board['11'] == 'O' and board['22'] == 'O':

            print('{} won !'.format(O))
            return 1
        if board['00'] == 'O' and board['10'] == 'O' and board['20'] == 'O':

            print('{} won !'.format(O))
            return 1
        if board['01'] == 'O' and board['11'] == 'O' and board['21'] == 'O':
            print('{} won !'.format(O))
            return 1
        if board['02'] == 'O' and board['12'] == 'O' and board['22'] == 'O':
            print('{} won !'.format(O))
            return 1
        return 0

    moves = 0
    end_check=0
    while True:
        print(color.BOLD+board['00']+'\t'+board['01']+'\t'+board['02']+'\n')
        print(color.BOLD+board['10']+'\t'+board['11']+'\t'+board['12']+'\n')
        print(color.BOLD+board['20']+'\t'+board['21']+'\t'+board['22']+'\n')
        end_check = check()
        
        if moves ==8 or end_check==1:
            if moves==8:
                print("it's a tie:\n")
            play=input("would You like to play again? (Y/N): ")
            if play.upper()=='Y':
                play_again()
            else:
                print("bye!")
                break
        while True:
            if name == X:
                print("Player of current Turn: {}".format(name))
                while True:
                    row = int(input("Choose a row number from 0 to 2:"))
                    if row>2 or row<0:
                        print("{} is not a valid row".format(row))
                    else:
                        break
                while True:
                    column = int(input("Choose a column number from 0 to 2:"))
                    if column>2 or column<0:
                        print("{} is not a valid column".format(column))
                    else:
                        break
                s = str(row)+str(column)
                if s in board and board[s]=='.':
                    board[s] = "X"
                    name = O
                    break
                else:
                    print('Invalid input, try again')
                    continue
            else:
                print("Player of current Turn: {}".format(name))
                while True:
                    row = int(input("Choose a row number from 0 to 2:"))
                    if row>2 or row<0:
                        print("{} is not a valid row".format(row))
                    else:
                        break
                while True:
                    column = int(input("Choose a column number from 0 to 2:"))
                    if column>2 or column<0:
                        print("{} is not a valid column".format(column))
                    else:
                        break
                s = str(row)+str(column)
                if s in board and board[s]=='.':
                    board[s] = "O"
                    name = X
                    break
                else:
                    print('Invalid input, try again')
                    continue   
            moves+=1    
play_again()

