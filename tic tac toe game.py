# initialize player and opponent
player,opponent='x','o'

# create a function to return if next move available or not
def moveavailable (board):
    for i in range(3):
        for j in range(3):
            return True
    return False

# create a function to evaluate the board  and give result who wins
def evaluate (board) :
    # check the board by row wise
    for row in range(3):
        if(board[row][0]==board[row][1] and board[row][1]==board[row][2]):
            if(board[row][0]==player):
                return 10
            elif(board[row][0]==opponent):
                return -10
    # check the board by column wise
    for col in range(3):
        if(board[0][col]==board[1][col] and board[1][col]==board[2][col]):
            if (board[0][col] == player):
                return 10
            elif (board[0][col] == opponent):
                return -10
    # now check the board in diagonal direction
    if(board[0][2]==board[1][1] and board[1][1]==board[2][0]):
        if(board[0][2]==player):
            return 10
        elif(board[0][2]==opponent):
            return -10

    if(board[0][0]==board[1][1] and board[1][1]==board[2][2]):
        if(board[0][0]==player):
            return 10
        elif(board[0][0]==opponent):
            return -10

    return 0

def minimax(board,depth,Max):
    value=evaluate(board)

    if(value==10):  # for the player's win
        return value
    if(value==-10):  # for the opponent's win
        return value
    if(moveavailable(board)==False):  # if the match draw
        return 0
    #if it's a player move
    if(Max):
        best_value=-1000
        for i in range(3):
            for j in range(3):
                if( board[i][j] == '_' ): #check for the empty cell
                    board[i][j]=player
                    best_value=max(best_value,minimax(board,depth+1,not Max)) # recursive call to find the maximum value
                    board[i][j]='_'
        return best_value

    else:  # if it's opponents move
        best_value=1000
        for i in range(3):
            for j in range(3):
                if (board[i][j] == '_'):  # check for the empty cell
                    board[i][j] = opponent
                    best_value = min(best_value,
                                     minimax(board, depth + 1,not Max))  # recursive call to find the minimum value
                    board[i][j] = '_'
        return best_value

def best_move(board):
    bestvalue=-1000
    best_mov=(-1,-1)

    for i in range(3):
        for j in range(3):
            if (board[i][j] == '_'):
                board[i][j]=player
                move_value=minimax(board,0,False)
                board[i][j]='_'
                if(move_value>bestvalue):
                    best_mov=(i,j)
                    bestvalue=move_value
    print("The value of best move",bestvalue)
    print()
    return best_mov


# main code of tic tac toe minimax algorithm

if __name__ == '__main__':
    board=[
        ['x', 'o', 'x'],
        ['_', '_', '_'],
        ['o', 'o', 'x']
    ]
    optimalmove=best_move(board)
    print("The optimal move for the given situation is ROW:",optimalmove[0],"COLUMN:",optimalmove[1])













