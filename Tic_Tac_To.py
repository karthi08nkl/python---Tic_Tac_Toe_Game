def display_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

def check_win(board,player):
    
    win_conditions = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False  

def check_tie(board):

    for spot in board:
        if spot != 'X' and spot != 'O':
            return False
    return True 

def valid_move(board,player):
    
    while True:
        try:
            check = int(input(f"Player{player}, Enter a Number from (1-9) : "))
            index = check - 1

            if index < 0 or index > 8:
                print("Invalid Number!")
            elif board[index] == 'X'or board[index] == 'O':
                print("That spot is already taken")
            else:
                return index
        except ValueError:
            print("Invalid Choice! Choose number from(1-9) only")

def main():

    print("*** TIC-TAC-TOE ***")
    print("-----------------")
    print("Player 1 : X || Player 2: O")

    board = [str(i) for i in range (1,10)]
    current_player = 'X'

    while True:
        display_board(board)

        index = valid_move(board,current_player)
        board[index] = current_player

        if check_win(board,current_player):
            display_board(board)
            print(f"Player {current_player} won this game!")
            break


        if check_tie(board):
            display_board(board)
            print("It is a Tie Game!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()