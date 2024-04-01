import random
def start_game(players_list,players_score,game_status):
    print("Game Started")
    print(players_list,players_score,game_status)
    while game_status:
        for players_name in players_list:
            die_count=roll_the_dice()
            print(f"{players_name}:{die_count}")
            if(players_score[players_name]+die_count>100):
                print("Die not Count")
                print(players_name,players_score,game_status)
            else:
                players_score[players_name]=players_score[players_name]+die_count
                game_status=checking_winner(players_name,players_score)
                if(game_status):
                    players_name,players_score,game_status=checking_for_snakes_and_ladders(players_name,players_score,game_status)
                    print(players_name,players_score,game_status)
                else:
                    return f"Game finished winner is {players_name}"
    



def checking_for_snakes_and_ladders(players_name,players_score,game_status):
    snakes={97:78,95:56,88:24,62:18,48:26,36:6,32:10}
    ladder={1:38,4:14,8:30,21:42,28:76,50:67,71:92,80:99}
    score=players_score[players_name]
    if(score in snakes):
        players_score[players_name]=snakes[score]
        print(f"Player got hit by snake score decreased {players_score[players_name]}")
    elif(score in ladder):
        players_score[players_name]=ladder[score]
        print(f"Player got ladder score increased {players_score[players_name]}")
    else:
        print("Normal")
    return players_name,players_score,game_status
    
#declaring 0 to every player
def initial_setup(players_list):
    player_score={i:0 for i in players_list}
    return player_score

#check in the winner
def checking_winner(player_name,players_score):
    if(players_score[player_name]==100):
        return False
    else:
        return True
#Rolling the dice for the player
def roll_the_dice():
    count=random.randint(1,6)
    #print(count)
    return count
#Game Starts

def select_player(no_of_players):
    #creating no of players and starting the game
    if(no_of_players<=1):
        print("Players should be more than one")
    elif(no_of_players>4):
        print("Player had reached maximum. It should not be greater than 4")
    else:
        #print(f"There are {no_of_players} in the game")
        game_status=True
        players_list=["PLAYER-"+str(i+1) for i in range(no_of_players)]
        players_score=initial_setup(players_list)
        #print(players_list)
        #print(players_score)
        winner=start_game(players_list,players_score,game_status)
        print(winner)
    



no_of_players=4
select_player(no_of_players)
