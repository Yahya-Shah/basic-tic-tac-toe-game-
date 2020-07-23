#OLD CODE#
import itertools

def game_board (game_map, player=0, row=0, column=0, just_display= False):
    try:
        if game_map[row][column] != 0:
            print("This position is occuipied, choose another")
            return game_map, False

        print ("   "+"  ".join([str(i) for i in range(len(game_map))]))
        
        if just_display != True:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print (count, row)

        return game_map, True
    
    except IndexError as e:
        print("Wrong Choice Kindly Enter Valid Input as 0 1 or 2")
        return game_map, False


def win(current_game):

    def win_check(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
    
    #horizontal
    for row in game:
        print (row)
        if win_check(row):
            print(f"Player {row[0]} is the winner horzontally!(-)")
            return True

    #vertical
    for column in range(len(game)):
        check = []
        for row in game:
            check.append(row[column])
        if win_check(check): 
            print(f"Player {check[0]} is the winner vertically!(|)")
            return True

    #diagonal
    diag_right = []
    for column, row in enumerate(reversed(range(len(game)))):
        diag_right.append(game[row][column])
    if win_check(diag_right):
        print(f"Player {diag_right[0]} is the winner diagonally!(/)")
        return True

    diag_left = []
    for ix in range(len(game)):
        diag_left.append(game[ix][ix])
    if win_check(diag_left):
        print(f"Player {diag_left[0]} is the winner diagonally!(\\)")
        return True

    return False


def display():    
    global game
    play = True
    player = [1,2]

    while play:
        game_size = int(input("What game size of tic tac toe do you want to play? " ))
        game = [[0 for i in range(game_size)] for i in range(game_size)]
        game_won = False
        game, _ = game_board(game, just_display=True)
        player_choice = itertools.cycle([1,2])

        while not game_won:
            current_player = next(player_choice)
            print (f"current player {current_player}") 
            played = False

            while not played:
                column_choice = int(input("What column do you want to chose? (0,1,2): "))
                row_choice = int(input("What row do you want to chose? (0,1,2): "))
                game, played = game_board(game, player = current_player, row = row_choice , column = column_choice)
            
            if win(game):
                game_won = True
                again = input ("The game is over, do you want to play agai? (y/n) ")
                if again.lower() == "y":
                    print("restaring")
                elif again.lower() == "n":
                    print("Byeeeee!")
                    play = False
                else:
                    print("Not a valide choice")
                    play = False
                    
display()